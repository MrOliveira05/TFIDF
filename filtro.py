import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from tabulate import tabulate
avaliacoes = pd.read_csv('ratings.csv', sep='\t', encoding='latin-1', usecols=['user_id', 'movie_id', 'rating'])
usuarios = pd.read_csv('users.csv', sep='\t', encoding='latin-1', usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])
filmes = pd.read_csv('movies.csv', sep='\t', encoding='latin-1', usecols=['movie_id', 'title', 'genres'])
def genre_recommendations(title):
    idx = indices[title]
    sim_pontos = list(enumerate(simicos[idx]))
    sim_pontos = sorted(sim_pontos, key=lambda x: x[1])
    sim_pontos = sim_pontos[1:21]
    movie_indices = [i[0] for i in sim_pontos]
    Func = open("ListaRecomenda.html","w") 
    Func.write("<html>\n<head>\n<title> \nRecomendação Filmes \ </title>\n</head> <body "\
               "style='background-color:powderblue;'><h1>Recomendação de filmes usando <u>similaridade de cossenos"\
                "</u></h1> \n<h2>"+tabulate(titles.iloc[movie_indices],tablefmt='html')+"</h2>\n</body></html>") 
    Func.close()
    return titles.iloc[movie_indices]
filmes['genres'] = filmes['genres'].str.split('|')
filmes['genres'] = filmes['genres'].fillna("").astype('str')
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(filmes['genres'])
tfidf_matrix.shape
simicos = linear_kernel(tfidf_matrix, tfidf_matrix)
simicos[:4, :4]
titles = filmes['title']
indices = pd.Series(filmes.index, index=filmes['title'])

