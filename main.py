# import streamlit as st
# from processing import preprocess
# from processing import display
# import pandas as pd
# import requests
# import ast
# import time

# # Page configuration
# st.set_page_config(layout="wide", page_title="CineMatch", page_icon="🎬")

# # Add custom CSS
# st.markdown("""
#     # <style>
#     /* Global Styles */
#     [data-testid="stAppViewContainer"] {
#         background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
#     }
    
#     .hero {
#         text-align: center;
#         padding: 4rem 2rem;
#         background: rgba(30, 41, 59, 0.5);
#         border-radius: 20px;
#         margin: -6rem -4rem 2rem -4rem;
#         backdrop-filter: blur(10px);
#     }
    
#     .hero h1 {
#         font-size: 4rem;
#         font-weight: 800;
#         background: linear-gradient(45deg, #60a5fa, #a78bfa);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         margin-bottom: 1rem;
#     }
    
#     .hero p {
#         color: #94a3b8;
#         font-size: 1.2rem;
#     }
    
#     /* Search Section */
#     .search-container {
#         background: rgba(30, 41, 59, 0.7);
#         padding: 2rem;
#         border-radius: 15px;
#         backdrop-filter: blur(10px);
#         border: 1px solid rgba(148, 163, 184, 0.1);
#         max-width: 800px;
#         margin: 0 auto;
#     }
    
#     /* Movie Details */
#     .movie-header {
#         height: 300px;
#         background: linear-gradient(to bottom, rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.4));
#         border-radius: 20px;
#         margin-bottom: 2rem;
#     }
    
#     .movie-poster-card {
#         position: relative;
#         margin-top: -150px;
#     }
    
#     .movie-poster-card img {
#         border-radius: 15px;
#         box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
#         transition: transform 0.3s ease;
#     }
    
#     .rating-badge {
#         position: absolute;
#         top: 10px;
#         right: 10px;
#         background: linear-gradient(45deg, #f59e0b, #f97316);
#         color: white;
#         padding: 0.5rem 1rem;
#         border-radius: 20px;
#         font-weight: bold;
#     }
    
#     /* Recommendations Grid */
#     .recommendations-grid {
#         display: grid;
#         grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
#         gap: 2rem;
#         padding: 2rem;
#     }
    
#     .movie-card {
#         background: rgba(30, 41, 59, 0.7);
#         border-radius: 15px;
#         overflow: hidden;
#         transition: transform 0.3s ease;
#         border: 1px solid rgba(148, 163, 184, 0.1);
#     }
    
#     .movie-card:hover {
#         transform: translateY(-5px);
#     }
    
#     .movie-info {
#         padding: 1rem;
#     }
    
#     .movie-info h3 {
#         color: white;
#         font-size: 1rem;
#         margin-bottom: 0.5rem;
#     }
    
#     /* Custom Buttons */
#     .custom-button {
#         background: linear-gradient(45deg, #3b82f6, #6366f1);
#         color: white;
#         padding: 0.5rem 1.5rem;
#         border-radius: 10px;
#         border: none;
#         cursor: pointer;
#         transition: all 0.3s ease;
#     }
    
#     .custom-button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
#     }
    
#     /* Movie Details Styling */
#     .movie-container {
#         background: rgba(15, 23, 42, 0.9);
#         border-radius: 20px;
#         padding: 2rem;
#         margin-bottom: 3rem;
#         backdrop-filter: blur(10px);
#     }
    
#     .movie-details {
#         color: #fff;
#         padding: 1rem 2rem;
#     }
    
#     .overview-section {
#         background: rgba(255, 255, 255, 0.1);
#         padding: 1.5rem;
#         border-radius: 15px;
#         margin-top: 1.5rem;
#     }
    
#     .overview-section h3 {
#         color: #60a5fa;
#         margin-bottom: 1rem;
#         font-size: 1.3rem;
#     }
    
#     .overview-section p {
#         color: #e2e8f0;
#         line-height: 1.6;
#         font-size: 1.1rem;
#     }
    
#     /* Recommendations Grid Styling */
#     .recommendations-grid {
#         display: grid;
#         grid-template-columns: repeat(4, 1fr);
#         gap: 1.5rem;
#         padding: 1rem;
#     }
    
#     .recommendation-card {
#         position: relative;
#         border-radius: 12px;
#         overflow: hidden;
#         aspect-ratio: 2/3;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         transition: transform 0.3s ease;
#     }
    
#     .recommendation-card img {
#         width: 100%;
#         height: 100%;
#         object-fit: cover;
#     }
    
#     .movie-overlay {
#         position: absolute;
#         bottom: 0;
#         left: 0;
#         right: 0;
#         background: linear-gradient(transparent, rgba(0, 0, 0, 0.9));
#         padding: 1rem;
#         transform: translateY(100%);
#         transition: transform 0.3s ease;
#     }
    
#     .recommendation-card:hover {
#         transform: translateY(-5px);
#     }
    
#     .recommendation-card:hover .movie-overlay {
#         transform: translateY(0);
#     }
    
#     .movie-overlay h3 {
#         color: white;
#         font-size: 1rem;
#         text-align: center;
#         margin: 0;
#     }
    
#     /* Search Bar Styling */
#     [data-testid="stTextInput"] {
#         background: rgba(255,255,255,0.1);
#         border-radius: 20px;
#         padding: 5px 15px;
#     }
    
#     /* Movie Details Layout */
#     .movie-poster-container {
#         position: relative;
#         width: 100%;
#         margin-bottom: 2rem;
#     }
    
#     .movie-poster-container img {
#         width: 100%;
#         border-radius: 15px;
#         box-shadow: 0 4px 20px rgba(0,0,0,0.3);
#     }
    
#     .rating-badge {
#         position: absolute;
#         top: 10px;
#         right: 10px;
#         background: linear-gradient(45deg, #f59e0b, #f97316);
#         color: white;
#         padding: 0.5rem 1rem;
#         border-radius: 20px;
#         font-weight: bold;
#     }
    
#     .movie-info-container {
#         background: rgba(15,23,42,0.8);
#         padding: 2rem;
#         border-radius: 15px;
#         backdrop-filter: blur(10px);
#         height: 100%;
#         margin-left: 2rem;
#     }
    
#     /* Search Bar Styling */
#     [data-testid="stTextInput"] {
#         background: rgba(255,255,255,0.1);
#         border-radius: 20px;
#         padding: 5px 15px;
#         margin-bottom: 1rem;
#     }
    
#     /* Ensure columns have proper gap */
#     [data-testid="column"] {
#         padding: 0 1rem;
#     }
    
#     /* Recommendations Grid */
#     .recommendations-title {
#         color: #fff;
#         margin: 2rem 0 1rem 0;
#         font-size: 1.5rem;
#     }
    
#     .movie-card {
#         position: relative;
#         border-radius: 8px;
#         overflow: hidden;
#         aspect-ratio: 2/3;
#         margin: 0.5rem;
#         cursor: pointer;
#         max-width: 150px;  /* Limit maximum width */
#         margin: 0 auto;    /* Center the card */
#     }
    
#     .movie-card img {
#         width: 100%;
#         height: 100%;
#         object-fit: cover;
#         transition: transform 0.3s ease;
#     }
    
#     .card-overlay {
#         position: absolute;
#         bottom: 0;
#         left: 0;
#         right: 0;
#         background: linear-gradient(transparent, rgba(0,0,0,0.9));
#         padding: 0.5rem;
#         transform: translateY(100%);
#         transition: transform 0.3s ease;
#     }
    
#     .movie-card:hover .card-overlay {
#         transform: translateY(0);
#     }
    
#     .card-overlay h3 {
#         color: white;
#         font-size: 0.8rem;
#         text-align: center;
#         margin: 0;
#         overflow: hidden;
#         text-overflow: ellipsis;
#         display: -webkit-box;
#         -webkit-line-clamp: 2;
#         -webkit-box-orient: vertical;
#     }
    
#     /* Ensure columns have proper spacing */
#     [data-testid="column"] {
#         padding: 0.25rem !important;
#     }
    
#     # /* Search Dropdown Styling */
#     # .stSelectbox {
#     #     background: rgba(30, 41, 59, 0.7);
#     #     border-radius: 10px;
#     #     backdrop-filter: blur(10px);
#     }
    
#     .stSelectbox > div > div {
#         background: transparent !important;
#         border: 1px solid rgba(255, 255, 255, 0.1) !important;
#     }
    
#     .stSelectbox [data-baseweb="select"] {
#         border-radius: 10px;
#     }
    
#     .stSelectbox [data-baseweb="popup"] {
#         background: rgba(30, 41, 59, 0.95) !important;
#         backdrop-filter: blur(10px);
#         border: 1px solid rgba(255, 255, 255, 0.1) !important;
#     }
    
#     .stSelectbox [data-baseweb="option"] {
#         padding: 8px 16px !important;
#     }
    
#     .stSelectbox [data-baseweb="option"]:hover {
#         background: rgba(59, 130, 246, 0.2) !important;
#     }
    
#     .movie-grid {
#         display: grid;
#         grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
#         gap: 2rem;
#         padding: 2rem 0;
#     }
    
#     .movie-card {
#         position: relative;
#         transition: transform 0.3s ease;
#         cursor: pointer;
#     }
    
#     .movie-card:hover {
#         transform: translateY(-10px);
#     }
    
#     .movie-info {
#         position: absolute;
#         bottom: 0;
#         left: 0;
#         right: 0;
#         background: linear-gradient(transparent, rgba(0,0,0,0.9));
#         padding: 1rem;
#         color: white;
#     }
    
#     .movie-header {
#         display: flex;
#         gap: 2rem;
#         margin-bottom: 2rem;
#     }
    
#     .movie-poster {
#         flex: 0 0 300px;
#         border-radius: 15px;
#         overflow: hidden;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.2);
#     }
    
#     .movie-meta {
#         display: flex;
#         gap: 1rem;
#         flex-wrap: wrap;
#         margin: 1rem 0;
#     }
    
#     .meta-tag {
#         background: rgba(255,255,255,0.1);
#         padding: 0.5rem 1rem;
#         border-radius: 20px;
#         font-size: 0.9rem;
#     }
    
#     /* Hide Streamlit's fullscreen button */
#     button[title="View fullscreen"] {
#         display: none !important;
#     }
    
#     /* Remove pointer cursor from images */
#     .stImage > img {
#         cursor: default !important;
#     }
    
#     /* Remove link styling */
#     a {
#         text-decoration: none !important;
#         color: inherit !important;
#         pointer-events: none !important;
#     }
    
#     /* Remove link styling for all text elements */
#     p, h1, h2, h3, h4, h5, h6, span {
#         text-decoration: none !important;
#         color: inherit !important;
#     }
    
#     /* Remove link symbols from headers */
#     .st-emotion-cache-ztfqz8 a {
#         display: none !important;
#     }
    
#     /* Remove header hover effect */
#     .st-emotion-cache-ztfqz8:hover {
#         text-decoration: none !important;
#     }
    
#     /* Remove link styling from all headers */
#     h1, h2, h3, h4, h5, h6 {
#         text-decoration: none !important;
#     }
    
#     /* Remove anchor links */
#     .anchor-link {
#         display: none !important;
#     }
    
#     /* Remove all anchor links and their styling */
#     .stMarkdown a {
#         display: none !important;
#     }
    
#     /* Remove header link styling */
#     h1, h2, h3, h4, h5, h6 {
#         text-decoration: none !important;
#     }
    
#     /* Remove anchor hover effects */
#     .header-anchor {
#         display: none !important;
#     }
    
#     /* Remove Streamlit's default header styling */
#     .st-emotion-cache-ztfqz8 a,
#     .st-emotion-cache-16idsys a,
#     .st-emotion-cache-5rimss a {
#         display: none !important;
#     }
    
#     /* Prevent header hover effects */
#     .st-emotion-cache-ztfqz8:hover,
#     .st-emotion-cache-16idsys:hover,
#     .st-emotion-cache-5rimss:hover {
#         text-decoration: none !important;
#     }
#     .stApp {
#         color: white !important;
#     }
#     .stSelectbox {
#         color: white !important;
#     }
#     .stSelectbox > div > div {
#         color: white !important;
#     }
#     /* Make dropdown text white */
#     .stSelectbox div[data-baseweb="select"] span {
#         color: white !important;
#     }
#     /* Make dropdown options white */
#     .stSelectbox div[role="listbox"] li {
#         color: white !important;
#     }
#     /* Make placeholder text white with slight transparency */
#     .stSelectbox div[data-baseweb="select"] div[aria-selected="true"] {
#         color: rgba(255, 255, 255, 0.7) !important;
#     }
#     /* Make all text elements white by default */
#     p, h1, h2, h3, h4, h5, h6, span, div {
#         color: white !important;
#     }
#     .movie-details p {
#         color: white !important;
#     }
#     .movie-details span {
#         color: white !important;
#     }
#     .movie-meta-data {
#         color: white !important;
#     }
#     .overview-text {
#         color: white !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Initialize session state variables
# if "selected_movie_name" not in st.session_state:
#     st.session_state["selected_movie_name"] = None

# if "show_recommendations" not in st.session_state:
#     st.session_state["show_recommendations"] = True

# # TMDB API key
# TMDB_API_KEY = "6bc3065293c944b5ad11cb7cd15c076e"

# def fetch_posters(movie_id):
#     """
#     Fetch the poster URL for a given movie ID using TMDB API.
#     """
#     response = requests.get(
#         f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
#     )
#     data = response.json()
#     try:
#         return f"https://image.tmdb.org/t/p/w780/{data['poster_path']}"
#     except KeyError:
#         return "https://via.placeholder.com/150"

# def recommend_display(new_df):
#     """
#     Display movie recommendations and handle movie selection with a predictive dropdown.
#     """
#     st.markdown("<h1 class='title'>🎥 Movie Recommender</h1>", unsafe_allow_html=True)
#     st.markdown("<div class='recommend-section'>", unsafe_allow_html=True)

#     # Predictive dropdown for initial movie search
#     search_query = st.selectbox(
#         "Search for a Movie:",
#         options=[""] + new_df["title"].dropna().unique().tolist(),
#         format_func=lambda x: "Type to search..." if x == "" else x,
#         key="initial_movie_search"
#     )

#     recommend_button = st.button("Get Recommendations")
#     if recommend_button:
#         if search_query and search_query != "Type to search...":
#             st.session_state["selected_movie_name"] = search_query
#             st.session_state["show_recommendations"] = False
#             st.experimental_rerun()
#         else:
#             st.warning("Please select or enter a movie name.")

# def display_movie_details_and_recommendations(new_df):
#     # Add this CSS at the start of the function
#     st.markdown("""
#         <style>
#         /* Hide Streamlit's fullscreen button */
#         button[title="View fullscreen"] {
#             display: none !important;
#         }
        
#         /* Remove pointer cursor from images */
#         .stImage > img {
#             cursor: default !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)
    
#     selected_movie_name = st.session_state.get("selected_movie_name", None)
    
#     if selected_movie_name:
#         try:
#             movie_details = preprocess.get_details(selected_movie_name)
            
#             if movie_details:
#                 # Main movie details section
#                 col_poster, col_info = st.columns([1, 2], gap="large")
                
#                 with col_poster:
#                     st.markdown(f'''
#                         <div style="position: relative;">
#                             <img src="{movie_details[0]}" 
#                                  style="width: 100%; 
#                                         border-radius: 10px; 
#                                         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#                                         pointer-events: none;">
#                             <div style="position: absolute; 
#                                       top: 10px; 
#                                       right: 10px; 
#                                       background: rgba(0,0,0,0.7); 
#                                       padding: 5px 10px; 
#                                       border-radius: 20px; 
#                                       color: gold;">
#                                 ★ {movie_details[8]}/10
#                             </div>
#                         </div>
#                     ''', unsafe_allow_html=True)
                
#                 with col_info:
#                     st.markdown(f"""
#                         <div style="font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem; color: white;">
#                             {selected_movie_name}
#                         </div>
#                     """, unsafe_allow_html=True)
                    
#                     # First, add Material Design Icons CDN at the start of your function
#                     st.markdown("""
#                         <link href="https://cdn.jsdelivr.net/npm/@mdi/font@7.2.96/css/materialdesignicons.min.css" rel="stylesheet">
#                         <style>
#                             .mdi {
#                                 font-size: 1.4rem;
#                                 vertical-align: middle;
#                             }
#                         </style>
#                     """, unsafe_allow_html=True)
                    
#                     # Then replace the metadata section with this enhanced version
#                     st.markdown(f"""
#                         <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
#                             <span style="background: linear-gradient(135deg, #1a237e 0%, #0d47a1 100%); 
#                                         padding: 0.7rem 1.2rem; 
#                                         border-radius: 20px; 
#                                         display: flex; 
#                                         align-items: center; 
#                                         gap: 0.7rem;
#                                         box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
#                                 <i class="mdi mdi-calendar-star" style="color: #82b1ff;"></i>
#                                 {movie_details[4]}
#                             </span>
#                             <span style="background: linear-gradient(135deg, #311b92 0%, #4527a0 100%); 
#                                         padding: 0.7rem 1.2rem; 
#                                         border-radius: 20px; 
#                                         display: flex; 
#                                         align-items: center; 
#                                         gap: 0.7rem;
#                                         box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
#                                 <i class="mdi mdi-timer-outline" style="color: #b388ff;"></i>
#                                 {movie_details[6]} min
#                             </span>
#                             <span style="background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%); 
#                                         padding: 0.7rem 1.2rem; 
#                                         border-radius: 20px; 
#                                         display: flex; 
#                                         align-items: center; 
#                                         gap: 0.7rem;
#                                         box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
#                                 <i class="mdi mdi-currency-usd" style="color: #69f0ae;"></i>
#                                 ${"{:,.0f}".format(float(movie_details[1]))}
#                             </span>
#                             <span style="background: linear-gradient(135deg, #bf360c 0%, #d84315 100%); 
#                                         padding: 0.7rem 1.2rem; 
#                                         border-radius: 20px; 
#                                         display: flex; 
#                                         align-items: center; 
#                                         gap: 0.7rem;
#                                         box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
#                                 <i class="mdi mdi-star-face" style="color: #ffab91;"></i>
#                                 {movie_details[8]}/10
#                             </span>
#                         </div>
#                     """, unsafe_allow_html=True)
                    
#                     st.markdown("""
#                         <div style="font-size: 1.5rem; font-weight: bold; margin: 1.5rem 0 1rem 0; color: white;">
#                             Overview
#                         </div>
#                     """, unsafe_allow_html=True)
#                     st.write(movie_details[3])
                
#                 # Cast section with custom styling
#                 st.markdown("""
#                     <div style="font-size: 1.5rem; font-weight: bold; margin: 1.5rem 0 1rem 0; color: white;">
#                         Cast
#                     </div>
#                 """, unsafe_allow_html=True)
#                 cast_cols = st.columns(4)
#                 for idx, (cast_id, cast_name) in enumerate(zip(movie_details[14][:4], movie_details[11][:4])):
#                     with cast_cols[idx]:
#                         url, bio = fetch_person_details(cast_id)
#                         st.markdown(f'''
#                             <div style="text-align: center;">
#                                 <img src="{url}" 
#                                      style="width: 120px; 
#                                             height: 180px; 
#                                             object-fit: cover; 
#                                             border-radius: 10px; 
#                                             margin-bottom: 0.5rem;
#                                             pointer-events: none;">
#                                 <p style="margin: 0; 
#                                           font-weight: bold; 
#                                           text-decoration: none; 
#                                           color: white;">
#                                     {cast_name}
#                                 </p>
#                             </div>
#                         ''', unsafe_allow_html=True)
                
#                 # Recommendations section
#                 st.markdown("""
#                     <div style="font-size: 2rem; font-weight: bold; text-align: center; margin: 3rem 0 2rem 0; color: white;">
#                         You May Also Like
#                     </div>
#                 """, unsafe_allow_html=True)

#                 recommended_movies, posters = preprocess.recommend(
#                     new_df, selected_movie_name, r"Files/similarity_tags_tags.pkl"
#                 )

#                 # Display recommendations in a grid
#                 cols = st.columns(4)
#                 for idx, (movie, poster) in enumerate(zip(recommended_movies[:8], posters[:8])):
#                     with cols[idx % 4]:
#                         rec_details = preprocess.get_details(movie)
#                         st.markdown(f'''
#                             <div style="background: rgba(255,255,255,0.05); 
#                                         padding: 1rem; 
#                                         border-radius: 10px; 
#                                         margin-bottom: 1rem;
#                                         transition: transform 0.3s ease;">
#                                 <img src="{poster}" 
#                                      style="width: 100%; 
#                                             border-radius: 8px; 
#                                             margin-bottom: 0.5rem;">
#                                 <h4 style="margin: 0.5rem 0; 
#                                            color: white;">
#                                     {movie}
#                                 </h4>
#                                 <p style="font-size: 0.8rem;
#                                           color: rgba(255,255,255,0.7);
#                                           margin: 0.5rem 0;">
#                                     {rec_details[3][:100]}...
#                                 </p>
#                                 <div style="display: flex; 
#                                             justify-content: space-between; 
#                                             align-items: center;
#                                             margin: 0.5rem 0;">
#                                     <span style="color: gold;">★ {rec_details[8]}/10</span>
#                                     <span style="color: rgba(255,255,255,0.6);">
#                                         {rec_details[4]}
#                                     </span>
#                                 </div>
#                             </div>
#                         ''', unsafe_allow_html=True)
                        
#                         # Custom styled button
#                         st.markdown(f'''
#                             <div onclick="document.getElementById('movie_button_{idx}').click()"
#                                  style="background: linear-gradient(45deg, #3b82f6, #6366f1);
#                                         color: white;
#                                         text-align: center;
#                                         padding: 0.5rem;
#                                         border-radius: 8px;
#                                         cursor: pointer;
#                                         transition: all 0.3s ease;
#                                         box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);">
#                                 View Details
#                             </div>
#                         ''', unsafe_allow_html=True)
                        
#                         # Hidden button for handling clicks
#                         if st.button("", key=f"movie_button_{idx}", help=f"View {movie}"):
#                             st.session_state.selected_movie_name = movie
#                             st.experimental_rerun()
                            
#         except Exception as e:
#             st.error(f"Error loading movie details: {str(e)}")

# def fetch_person_details(id_):
#     data = requests.get(
#         'https://api.themoviedb.org/3/person/{}?api_key=6177b4297dff132d300422e0343471fb'.format(id_)).json()

#     try:
#         url = 'https://image.tmdb.org/t/p/w220_and_h330_face' + data['profile_path']

#         if data['biography']:
#             biography = data['biography']
#         else:
#             biography = " "

#     except:
#         url = "https://media.istockphoto.com/vectors/error-icon-vector-illustration-vector-id922024224?k=6&m" \
#               "=922024224&s=612x612&w=0&h=LXl8Ul7bria6auAXKIjlvb6hRHkAodTqyqBeA6K7R54="
#         biography = ""

#     return url, biography

# def create_hero_section(new_df):
#     st.markdown("""
#         <div style="
#             background: linear-gradient(135deg, rgba(13, 17, 23, 0.95) 0%, rgba(42, 25, 66, 0.95) 100%);
#             padding: 3rem 2rem;
#             border-radius: 24px;
#             margin: -6rem -4rem 4rem -4rem;
#             box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
#             backdrop-filter: blur(10px);
#             border: 1px solid rgba(255, 255, 255, 0.1);
#         ">
#             <div style="
#                 display: flex;
#                 align-items: center;
#                 justify-content: center;
#                 gap: 2rem;
#                 margin-bottom: 3rem;
#             ">
#                 <div class="logo" style="
#                     font-family: 'Montserrat', sans-serif;
#                     margin-bottom: 1.5rem;
#                 ">
#                     <div style="
#                         display: inline-flex;
#                         align-items: center;
#                         background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
#                         padding: 0.8rem 1.5rem;
#                         border-radius: 15px;
#                         box-shadow: 0 4px 15px rgba(255, 65, 108, 0.3);
#                         transform: rotate(-2deg);
#                     ">
#                         <span style="
#                             font-size: 3.5rem;
#                             font-weight: 800;
#                             background: linear-gradient(to right, #fff, #e0e0e0);
#                             -webkit-background-clip: text;
#                             -webkit-text-fill-color: transparent;
#                             margin-right: 0.5rem;
#                         ">Cine</span>
#                         <span style="
#                             font-size: 3.5rem;
#                             font-weight: 800;
#                             color: #fff;
#                             position: relative;
#                         ">Match
#                             <svg width="30" height="30" viewBox="0 0 24 24" style="
#                                 position: absolute;
#                                 top: -10px;
#                                 right: -20px;
#                                 fill: #FFD700;
#                             ">
#                                 <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
#                             </svg>
#                         </span>
#                     </div>
#                 </div>
#             </div>
#         </div>
        
#         <style>
#             @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap');
#         </style>
#     """, unsafe_allow_html=True)

#       # Add Streamlit search component in a container
#     with st.container():
#         col1, col2, col3 = st.columns([1,2,1])
#         with col2:
#             # Create a form for handling Enter key press
#             with st.form(key='search_form'):
#                 search_query = st.text_input(
#                     "",
#                     placeholder="Search movies...",
#                     key="movie_search"
#                 )
#                 submit_button = st.form_submit_button('Search', type="primary")
                
#                 if submit_button and search_query:
#                     movie_titles = sorted(new_df["title"].dropna().unique())
#                     matching_movies = [
#                         movie for movie in movie_titles
#                         if search_query.lower() in movie.lower()
#                     ]
#                     if matching_movies:
#                         st.session_state.selected_movie_name = matching_movies[0]
#                         st.experimental_rerun()
#                     else:
#                         st.error("No movies found matching your search.")

# def set_page_config():
#     st.set_page_config(
#         page_title="Movie Recommender",
#         page_icon="🎬",
#         layout="wide",
#         initial_sidebar_state="collapsed"
#     )
    
#     # Add custom CSS for the page
#     st.markdown("""
#         <style>
#             .stApp {
#                 background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
#                 color: white;
#             }
            
#             .stSelectbox > div > div {
#                 background-color: rgba(255, 255, 255, 0.05);
#                 color: white;
#             }
            
#             [data-testid="stHeader"] {
#                 background-color: rgba(0,0,0,0.5);
#                 backdrop-filter: blur(10px);
#             }
#         </style>
#     """, unsafe_allow_html=True)

# def main():
#     display_obj = display.Main()
#     display_obj.get_df()
#     new_df = display_obj.new_df
    
#     # Create the hero section with search
#     create_hero_section(new_df)
    
#     # Display movie details if a movie is selected
#     if "selected_movie_name" in st.session_state and st.session_state.selected_movie_name:
#         display_movie_details_and_recommendations(new_df)

# if __name__ == "__main__":
#     main()












import streamlit as st
from processing import preprocess
from processing import display
import pandas as pd
import requests
import ast
import time

# Page configuration
st.set_page_config(layout="wide", page_title="CineMatch", page_icon="🎬")

# Add custom CSS
st.markdown("""
    <style>
    /* Global Styles */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    .hero {
        text-align: center;
        padding: 4rem 2rem;
        background: rgba(30, 41, 59, 0.5);
        border-radius: 20px;
        margin: -6rem -4rem 2rem -4rem;
        backdrop-filter: blur(10px);
    }
    
    .hero h1 {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(45deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .hero p {
        color: #94a3b8;
        font-size: 1.2rem;
    }
    
    /* Search Section */
    .search-container {
        background: rgba(30, 41, 59, 0.7);
        padding: 2rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(148, 163, 184, 0.1);
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Movie Details */
    .movie-header {
        height: 300px;
        background: linear-gradient(to bottom, rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.4));
        border-radius: 20px;
        margin-bottom: 2rem;
    }
    
    .movie-poster-card {
        position: relative;
        margin-top: -150px;
    }
    
    .movie-poster-card img {
        border-radius: 15px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease;
    }
    
    .rating-badge {
        position: absolute;
        top: 10px;
        right: 10px;
        background: linear-gradient(45deg, #f59e0b, #f97316);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
    }
    
    /* Recommendations Grid */
    .recommendations-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 2rem;
        padding: 2rem;
    }
    
    .movie-card {
        background: rgba(30, 41, 59, 0.7);
        border-radius: 15px;
        overflow: hidden;
        transition: transform 0.3s ease;
        border: 1px solid rgba(148, 163, 184, 0.1);
    }
    
    .movie-card:hover {
        transform: translateY(-5px);
    }
    
    .movie-info {
        padding: 1rem;
    }
    
    .movie-info h3 {
        color: white;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* Custom Buttons */
    .custom-button {
        background: linear-gradient(45deg, #3b82f6, #6366f1);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .custom-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    /* Movie Details Styling */
    .movie-container {
        background: rgba(15, 23, 42, 0.9);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 3rem;
        backdrop-filter: blur(10px);
    }
    
    .movie-details {
        color: #fff;
        padding: 1rem 2rem;
    }
    
    .overview-section {
        background: rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 15px;
        margin-top: 1.5rem;
    }
    
    .overview-section h3 {
        color: #60a5fa;
        margin-bottom: 1rem;
        font-size: 1.3rem;
    }
    
    .overview-section p {
        color: #e2e8f0;
        line-height: 1.6;
        font-size: 1.1rem;
    }
    
    /* Recommendations Grid Styling */
    .recommendations-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
        padding: 1rem;
    }
    
    .recommendation-card {
        position: relative;
        border-radius: 12px;
        overflow: hidden;
        aspect-ratio: 2/3;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .recommendation-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    .movie-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(transparent, rgba(0, 0, 0, 0.9));
        padding: 1rem;
        transform: translateY(100%);
        transition: transform 0.3s ease;
    }
    
    .recommendation-card:hover {
        transform: translateY(-5px);
    }
    
    .recommendation-card:hover .movie-overlay {
        transform: translateY(0);
    }
    
    .movie-overlay h3 {
        color: white;
        font-size: 1rem;
        text-align: center;
        margin: 0;
    }
    
    /* Search Bar Styling */
    [data-testid="stTextInput"] {
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 5px 15px;
    }
    
    /* Movie Details Layout */
    .movie-poster-container {
        position: relative;
        width: 100%;
        margin-bottom: 2rem;
    }
    
    .movie-poster-container img {
        width: 100%;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    
    .rating-badge {
        position: absolute;
        top: 10px;
        right: 10px;
        background: linear-gradient(45deg, #f59e0b, #f97316);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
    }
    
    .movie-info-container {
        background: rgba(15,23,42,0.8);
        padding: 2rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        height: 100%;
        margin-left: 2rem;
    }
    
    /* Search Bar Styling */
    [data-testid="stTextInput"] {
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 5px 15px;
        margin-bottom: 1rem;
    }
    
    /* Ensure columns have proper gap */
    [data-testid="column"] {
        padding: 0 1rem;
    }
    
    /* Recommendations Grid */
    .recommendations-title {
        color: #fff;
        margin: 2rem 0 1rem 0;
        font-size: 1.5rem;
    }
    
    .movie-card {
        position: relative;
        border-radius: 8px;
        overflow: hidden;
        aspect-ratio: 2/3;
        margin: 0.5rem;
        cursor: pointer;
        max-width: 150px;  /* Limit maximum width */
        margin: 0 auto;    /* Center the card */
    }
    
    .movie-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.3s ease;
    }
    
    .card-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(transparent, rgba(0,0,0,0.9));
        padding: 0.5rem;
        transform: translateY(100%);
        transition: transform 0.3s ease;
    }
    
    .movie-card:hover .card-overlay {
        transform: translateY(0);
    }
    
    .card-overlay h3 {
        color: white;
        font-size: 0.8rem;
        text-align: center;
        margin: 0;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    
    /* Ensure columns have proper spacing */
    [data-testid="column"] {
        padding: 0.25rem !important;
    }
    
    # /* Search Dropdown Styling */
    # .stSelectbox {
    #     background: rgba(30, 41, 59, 0.7);
    #     border-radius: 10px;
    #     backdrop-filter: blur(10px);
    }
    
    .stSelectbox > div > div {
        background: transparent !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    .stSelectbox [data-baseweb="select"] {
        border-radius: 10px;
    }
    
    .stSelectbox [data-baseweb="popup"] {
        background: rgba(30, 41, 59, 0.95) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    .stSelectbox [data-baseweb="option"] {
        padding: 8px 16px !important;
    }
    
    .stSelectbox [data-baseweb="option"]:hover {
        background: rgba(59, 130, 246, 0.2) !important;
    }
    
    .movie-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 2rem;
        padding: 2rem 0;
    }
    
    .movie-card {
        position: relative;
        transition: transform 0.3s ease;
        cursor: pointer;
    }
    
    .movie-card:hover {
        transform: translateY(-10px);
    }
    
    .movie-info {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(transparent, rgba(0,0,0,0.9));
        padding: 1rem;
        color: white;
    }
    
    .movie-header {
        display: flex;
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .movie-poster {
        flex: 0 0 300px;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .movie-meta {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin: 1rem 0;
    }
    
    .meta-tag {
        background: rgba(255,255,255,0.1);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
    }
    
    /* Hide Streamlit's fullscreen button */
    button[title="View fullscreen"] {
        display: none !important;
    }
    
    /* Remove pointer cursor from images */
    .stImage > img {
        cursor: default !important;
    }
    
    /* Remove link styling */
    a {
        text-decoration: none !important;
        color: inherit !important;
        pointer-events: none !important;
    }
    
    /* Remove link styling for all text elements */
    p, h1, h2, h3, h4, h5, h6, span {
        text-decoration: none !important;
        color: inherit !important;
    }
    
    /* Remove link symbols from headers */
    .st-emotion-cache-ztfqz8 a {
        display: none !important;
    }
    
    /* Remove header hover effect */
    .st-emotion-cache-ztfqz8:hover {
        text-decoration: none !important;
    }
    
    /* Remove link styling from all headers */
    h1, h2, h3, h4, h5, h6 {
        text-decoration: none !important;
    }
    
    /* Remove anchor links */
    .anchor-link {
        display: none !important;
    }
    
    /* Remove all anchor links and their styling */
    .stMarkdown a {
        display: none !important;
    }
    
    /* Remove header link styling */
    h1, h2, h3, h4, h5, h6 {
        text-decoration: none !important;
    }
    
    /* Remove anchor hover effects */
    .header-anchor {
        display: none !important;
    }
    
    /* Remove Streamlit's default header styling */
    .st-emotion-cache-ztfqz8 a,
    .st-emotion-cache-16idsys a,
    .st-emotion-cache-5rimss a {
        display: none !important;
    }
    
    /* Prevent header hover effects */
    .st-emotion-cache-ztfqz8:hover,
    .st-emotion-cache-16idsys:hover,
    .st-emotion-cache-5rimss:hover {
        text-decoration: none !important;
    }
    .stApp {
        color: white !important;
    }
    .stSelectbox {
        color: white !important;
    }
    .stSelectbox > div > div {
        color: white !important;
    }
    /* Make dropdown text white */
    .stSelectbox div[data-baseweb="select"] span {
        color: white !important;
    }
    /* Make dropdown options white */
    .stSelectbox div[role="listbox"] li {
        color: white !important;
    }
    /* Make placeholder text white with slight transparency */
    .stSelectbox div[data-baseweb="select"] div[aria-selected="true"] {
        color: rgba(255, 255, 255, 0.7) !important;
    }
    /* Make all text elements white by default */
    p, h1, h2, h3, h4, h5, h6, span, div {
        color: white !important;
    }
    .movie-details p {
        color: white !important;
    }
    .movie-details span {
        color: white !important;
    }
    .movie-meta-data {
        color: white !important;
    }
    .overview-text {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state variables
if "selected_movie_name" not in st.session_state:
    st.session_state["selected_movie_name"] = None

if "show_recommendations" not in st.session_state:
    st.session_state["show_recommendations"] = True

# TMDB API key
TMDB_API_KEY = "076aa064daba31efd326e9d7e5444c2d"

def fetch_posters(movie_id):
    """
    Fetch the poster URL for a given movie ID using TMDB API.
    """
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    )
    data = response.json()
    try:
        return f"https://image.tmdb.org/t/p/w780/{data['poster_path']}"
    except KeyError:
        return "https://via.placeholder.com/150"

def recommend_display(new_df):
    """
    Display movie recommendations and handle movie selection with a predictive dropdown.
    """
    st.markdown("<h1 class='title'>🎥 Movie Recommender</h1>", unsafe_allow_html=True)
    st.markdown("<div class='recommend-section'>", unsafe_allow_html=True)

    # Predictive dropdown for initial movie search
    search_query = st.selectbox(
        "Search for a Movie:",
        options=[""] + new_df["title"].dropna().unique().tolist(),
        format_func=lambda x: "Type to search..." if x == "" else x,
        key="initial_movie_search"
    )

    recommend_button = st.button("Get Recommendations")
    if recommend_button:
        if search_query and search_query != "Type to search...":
            st.session_state["selected_movie_name"] = search_query
            st.session_state["show_recommendations"] = False
            st.experimental_rerun()
        else:
            st.warning("Please select or enter a movie name.")

def display_movie_details_and_recommendations(new_df):
    # Add this CSS at the start of the function
    st.markdown("""
        <style>
        /* Hide Streamlit's fullscreen button */
        button[title="View fullscreen"] {
            display: none !important;
        }
        
        /* Remove pointer cursor from images */
        .stImage > img {
            cursor: default !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    selected_movie_name = st.session_state.get("selected_movie_name", None)
    
    if selected_movie_name:
        try:
            movie_details = preprocess.get_details(selected_movie_name)
            
            if movie_details:
                # Main movie details section
                col_poster, col_info = st.columns([1, 2], gap="large")
                
                with col_poster:
                    st.markdown(f'''
                        <div style="position: relative;">
                            <img src="{movie_details[0]}" 
                                 style="width: 100%; 
                                        border-radius: 10px; 
                                        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                                        pointer-events: none;">
                            <div style="position: absolute; 
                                      top: 10px; 
                                      right: 10px; 
                                      background: rgba(0,0,0,0.7); 
                                      padding: 5px 10px; 
                                      border-radius: 20px; 
                                      color: gold;">
                                ★ {movie_details[8]}/10
                            </div>
                        </div>
                    ''', unsafe_allow_html=True)
                
                with col_info:
                    st.markdown(f"""
                        <div style="font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem; color: white;">
                            {selected_movie_name}
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # First, add Material Design Icons CDN at the start of your function
                    st.markdown("""
                        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@7.2.96/css/materialdesignicons.min.css" rel="stylesheet">
                        <style>
                            .mdi {
                                font-size: 1.4rem;
                                vertical-align: middle;
                            }
                        </style>
                    """, unsafe_allow_html=True)
                    
                    # Then replace the metadata section with this enhanced version
                    st.markdown(f"""
                        <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
                            <span style="background: linear-gradient(135deg, #1a237e 0%, #0d47a1 100%); 
                                        padding: 0.7rem 1.2rem; 
                                        border-radius: 20px; 
                                        display: flex; 
                                        align-items: center; 
                                        gap: 0.7rem;
                                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                                <i class="mdi mdi-calendar-star" style="color: #82b1ff;"></i>
                                {movie_details[4]}
                            </span>
                            <span style="background: linear-gradient(135deg, #311b92 0%, #4527a0 100%); 
                                        padding: 0.7rem 1.2rem; 
                                        border-radius: 20px; 
                                        display: flex; 
                                        align-items: center; 
                                        gap: 0.7rem;
                                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                                <i class="mdi mdi-timer-outline" style="color: #b388ff;"></i>
                                {movie_details[6]} min
                            </span>
                            <span style="background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%); 
                                        padding: 0.7rem 1.2rem; 
                                        border-radius: 20px; 
                                        display: flex; 
                                        align-items: center; 
                                        gap: 0.7rem;
                                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                                <i class="mdi mdi-currency-usd" style="color: #69f0ae;"></i>
                                ${"{:,.0f}".format(float(movie_details[1]))}
                            </span>
                            <span style="background: linear-gradient(135deg, #bf360c 0%, #d84315 100%); 
                                        padding: 0.7rem 1.2rem; 
                                        border-radius: 20px; 
                                        display: flex; 
                                        align-items: center; 
                                        gap: 0.7rem;
                                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                                <i class="mdi mdi-star-face" style="color: #ffab91;"></i>
                                {movie_details[8]}/10
                            </span>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("""
                        <div style="font-size: 1.5rem; font-weight: bold; margin: 1.5rem 0 1rem 0; color: white;">
                            Overview
                        </div>
                    """, unsafe_allow_html=True)
                    st.write(movie_details[3])
                
                # Cast section with custom styling
                st.markdown("""
                    <div style="font-size: 1.5rem; font-weight: bold; margin: 1.5rem 0 1rem 0; color: white;">
                        Cast
                    </div>
                """, unsafe_allow_html=True)
                cast_cols = st.columns(4)
                for idx, (cast_id, cast_name) in enumerate(zip(movie_details[14][:4], movie_details[11][:4])):
                    with cast_cols[idx]:
                        url, bio = fetch_person_details(cast_id)
                        st.markdown(f'''
                            <div style="text-align: center;">
                                <img src="{url}" 
                                     style="width: 120px; 
                                            height: 180px; 
                                            object-fit: cover; 
                                            border-radius: 10px; 
                                            margin-bottom: 0.5rem;
                                            pointer-events: none;">
                                <p style="margin: 0; 
                                          font-weight: bold; 
                                          text-decoration: none; 
                                          color: white;">
                                    {cast_name}
                                </p>
                            </div>
                        ''', unsafe_allow_html=True)
                
                # Recommendations section
                st.markdown("""
                    <div style="font-size: 2rem; font-weight: bold; text-align: center; margin: 3rem 0 2rem 0; color: white;">
                        You May Also Like
                    </div>
                """, unsafe_allow_html=True)

                recommended_movies, posters = preprocess.recommend(
                    new_df, selected_movie_name, r"Files/similarity_tags_tags.pkl"
                )

                # Display recommendations in a grid
                cols = st.columns(4)
                for idx, (movie, poster) in enumerate(zip(recommended_movies[:8], posters[:8])):
                    with cols[idx % 4]:
                        rec_details = preprocess.get_details(movie)
                        st.markdown(f'''
                            <div style="background: rgba(255,255,255,0.05); 
                                        padding: 1rem; 
                                        border-radius: 10px; 
                                        margin-bottom: 1rem;
                                        transition: transform 0.3s ease;">
                                <img src="{poster}" 
                                     style="width: 100%; 
                                            border-radius: 8px; 
                                            margin-bottom: 0.5rem;">
                                <h4 style="margin: 0.5rem 0; 
                                           color: white;">
                                    {movie}
                                </h4>
                                <p style="font-size: 0.8rem;
                                          color: rgba(255,255,255,0.7);
                                          margin: 0.5rem 0;">
                                    {rec_details[3][:100]}...
                                </p>
                                <div style="display: flex; 
                                            justify-content: space-between; 
                                            align-items: center;
                                            margin: 0.5rem 0;">
                                    <span style="color: gold;">★ {rec_details[8]}/10</span>
                                    <span style="color: rgba(255,255,255,0.6);">
                                        {rec_details[4]}
                                    </span>
                                </div>
                            </div>
                        ''', unsafe_allow_html=True)
                        
                        # Custom styled button
                        st.markdown(f'''
                            <div onclick="document.getElementById('movie_button_{idx}').click()"
                                 style="background: linear-gradient(45deg, #3b82f6, #6366f1);
                                        color: white;
                                        text-align: center;
                                        padding: 0.5rem;
                                        border-radius: 8px;
                                        cursor: pointer;
                                        transition: all 0.3s ease;
                                        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);">
                                View Details
                            </div>
                        ''', unsafe_allow_html=True)
                        
                        # Hidden button for handling clicks
                        if st.button("", key=f"movie_button_{idx}", help=f"View {movie}"):
                            st.session_state.selected_movie_name = movie
                            st.experimental_rerun()
                            
        except Exception as e:
            st.error(f"Error loading movie details: {str(e)}")

def fetch_person_details(id_):
    data = requests.get(
        'https://api.themoviedb.org/3/person/{}?api_key=076aa064daba31efd326e9d7e5444c2d'.format(id_)).json()

    try:
        url = 'https://image.tmdb.org/t/p/w220_and_h330_face' + data['profile_path']

        if data['biography']:
            biography = data['biography']
        else:
            biography = " "

    except:
        url = "https://media.istockphoto.com/vectors/error-icon-vector-illustration-vector-id922024224?k=6&m" \
              "=922024224&s=612x612&w=0&h=LXl8Ul7bria6auAXKIjlvb6hRHkAodTqyqBeA6K7R54="
        biography = ""

    return url, biography

def create_hero_section(new_df):
    st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(13, 17, 23, 0.95) 0%, rgba(42, 25, 66, 0.95) 100%);
            padding: 3rem 2rem;
            border-radius: 24px;
            margin: -6rem -4rem 4rem -4rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        ">
            <div style="
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 2rem;
                margin-bottom: 3rem;
            ">
                <div class="logo" style="
                    font-family: 'Montserrat', sans-serif;
                    margin-bottom: 1.5rem;
                ">
                    <div style="
                        display: inline-flex;
                        align-items: center;
                        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
                        padding: 0.8rem 1.5rem;
                        border-radius: 15px;
                        box-shadow: 0 4px 15px rgba(255, 65, 108, 0.3);
                        transform: rotate(-2deg);
                    ">
                        <span style="
                            font-size: 3.5rem;
                            font-weight: 800;
                            background: linear-gradient(to right, #fff, #e0e0e0);
                            -webkit-background-clip: text;
                            -webkit-text-fill-color: transparent;
                            margin-right: 0.5rem;
                        ">Cine</span>
                        <span style="
                            font-size: 3.5rem;
                            font-weight: 800;
                            color: #fff;
                            position: relative;
                        ">Match
                            <svg width="30" height="30" viewBox="0 0 24 24" style="
                                position: absolute;
                                top: -10px;
                                right: -20px;
                                fill: #FFD700;
                            ">
                                <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                            </svg>
                        </span>
                    </div>
                </div>
            </div>
        </div>
        
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap');
        </style>
    """, unsafe_allow_html=True)

      # Add Streamlit search component in a container
    with st.container():
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            # Create a form for handling Enter key press
            with st.form(key='search_form'):
                search_query = st.text_input(
                    "",
                    placeholder="Search movies...",
                    key="movie_search"
                )
                submit_button = st.form_submit_button('Search', type="primary")
                
                if submit_button and search_query:
                    movie_titles = sorted(new_df["title"].dropna().unique())
                    matching_movies = [
                        movie for movie in movie_titles
                        if search_query.lower() in movie.lower()
                    ]
                    if matching_movies:
                        st.session_state.selected_movie_name = matching_movies[0]
                        st.experimental_rerun()
                    else:
                        st.error("No movies found matching your search.")

def set_page_config():
    st.set_page_config(
        page_title="Movie Recommender",
        page_icon="🎬",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Add custom CSS for the page
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
                color: white;
            }
            
            .stSelectbox > div > div {
                background-color: rgba(255, 255, 255, 0.05);
                color: white;
            }
            
            [data-testid="stHeader"] {
                background-color: rgba(0,0,0,0.5);
                backdrop-filter: blur(10px);
            }
        </style>
    """, unsafe_allow_html=True)

def main():
    display_obj = display.Main()
    display_obj.get_df()
    new_df = display_obj.new_df
    
    # Create the hero section with search
    create_hero_section(new_df)
    
    # Display movie details if a movie is selected
    if "selected_movie_name" in st.session_state and st.session_state.selected_movie_name:
        display_movie_details_and_recommendations(new_df)

if __name__ == "__main__":
    main()
