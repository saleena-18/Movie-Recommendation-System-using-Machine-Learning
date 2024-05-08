mkdir -p ~/.streamlit/

echo"\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml

# it will create an environment in the cloud itself.
# we will use this environment to install the required packages for our app.