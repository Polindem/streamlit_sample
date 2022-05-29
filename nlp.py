# core pkg
import streamlit as st 
import streamlit.components.v1 as stc

# EDA Pkgs
import pandas as pd

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Movie Directory App </h1>
    </div>
    """


def main():
	"""Basics on st.beta columns/layout"""
	
	menu = ["Home","Search","About"]
	choice = st.sidebar.selectbox("Menu",menu)
	stc.html(HTML_BANNER)

	df = pd.read_csv(r'/Users/polina/Desktop/herokau/movies__Polina_limpio_traducido_1.csv')

	


	if choice == 'Home':
		st.subheader("Home")


		# with st.beta_expander("titulo"):
		# 	mytext = st.text_area("Type Here")
		# 	st.write(mytext)
		# 	st.success("Hello")


		# st.dataframe(df)
		movies_titulo_list = df['titulo'].tolist()

		movie_choice = st.selectbox("Movie titulo",movies_titulo_list)
		with st.beta_expander('Movies DF',expanded=False):
			st.dataframe(df.head(10))

			# Filter
			link = df[df['titulo'] == movie_choice]['link'].values[0]
			titulo = df[df['titulo']== movie_choice]['titulo'].values
			descripcion = df[df['titulo']== movie_choice]['descripcion'].values


		# Layout
			# st.write(img_link)
			# st.image(img_link)
		c1,c2,c3 = st.beta_columns([1,2,1])

		with c1:
			with st.beta_expander("titulo"):
				st.success(titulo)


		with c2:
			with st.beta_expander("link"):
				st.success(link)


		with c3:
			with st.beta_expander("Description"):
				st.write(descripcion)





	elif choice == "Search":
		st.subheader("Search Movies")

		with st.beta_expander("Search By Year"):
			movie_year = st.number_input("Year",1995,2020)

			df_for_year = df[df['year'].dt.year == movie_year]
			st.dataframe(df_for_year)

		col1,col2,col3  = st.beta_columns([1,2,1])

		with col1:
			with st.beta_expander("titulo"):
				for t in df_for_year['titulo'].tolist():
					st.success(t)


		with col2:
			with st.beta_expander("link"):
				for i in df_for_year['link'].tolist():
					st.image(i)


		with col3:
			with st.beta_expander("descripcion"):
				for g in df_for_year['descripcion'].tolist():
					st.write(g)





		

	else:
		st.subheader("About")
		st.text("Built with Streamlit")
		st.text("pppppppp")



if __name__ == '__main__':
	main()

