# # Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.

# import streamlit as st
# from streamlit.logger import get_logger

# LOGGER = get_logger(__name__)


# def run():
#     st.set_page_config(
#         page_title="Hello",
#         page_icon="👋",
#     )

#     st.write("# Jukuri Shashank 👋")

#     st.sidebar.success("Select a demo above.")

#     st.markdown(
#         """
#         Streamlit is an open-source app framework built specifically for
#         Machine Learning and Data Science projects.
#         **👈 Select a demo from the sidebar** to see some examples
#         of what Streamlit can do!
#         ### Want to learn more?
#         - Check out [streamlit.io](https://streamlit.io)
#         - Jump into our [documentation](https://docs.streamlit.io)
#         - Ask a question in our [community
#           forums](https://discuss.streamlit.io)
#         ### See more complex demos
#         - Use a neural net to [analyze the Udacity Self-driving Car Image
#           Dataset](https://github.com/streamlit/demo-self-driving)
#         - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
#     """
#     )


# if __name__ == "__main__":
#     run()


import streamlit as st

# Add widgets and content to your app
st.title('Jukuri Shashank')
st.write('This is a simple Streamlit app.')
import streamlit as st

# Render a Markdown string
st.write("This is a **bold** and *italic* text.")

# Render a LaTeX expression
st.write("You can render LaTeX expressions like this: $e^{i\pi} + 1 = 0$")

# Render colored text
st.write("This is a <span style='color:red'>red</span> word." , unsafe_allow_html = True)

# Render emoji shortcode
st.write("You can use emoji shortcodes like :smile: to display 😀")

# Combine different elements in one st.write() call
st.write("You can combine **Markdown**, LaTeX, <span style='color:blue'>colored text</span>, and emojis :smile:", unsafe_allow_html=True)

# You can also use triple backticks to render code blocks
st.write("```python\nprint('Hello, Streamlit!')\n```")

st.write("")
st.write("**DATA FRAME**")

import streamlit as st
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
st.write(df)

import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


# import Streamlit as st

# try:
#     result = 1 / 0
# except Exception as e:

#     st.write(e)

import streamlit as st

# C code with an intentional error
c_code_with_error = """
#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}
"""

# Display the C code block with syntax highlighting (including the error)
st.code(c_code_with_error, language='c')

import streamlit as st

st.text("This is some text.")
# -------------------------------------------------------------------------------------------------------
st.divider()

import streamlit as st

latex = st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')  #Supported LaTeX functions are listed at https://katex.org/docs/supported.html.

import streamlit as st
st.slider("This is a slider", 0, 100, (25, 75))

st.divider()

import streamlit as st
import pandas as pd 

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating":4, "is_height": True},
        {"command": "st.balloons", "rating":5, "is_height": False},
        {"command": "st.time_input", "rating":6, "is_height": True},
    ]
)

st.dataframe(df, use_container_width = True)

st.divider()

import streamlit as st
import pandas as pd 

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

# df = load_data()
edited_df = st.data_editor(df) # 👈 An editable dataframe

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.divider()

import pandas as pd
import streamlit as st

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(
    df,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
    hide_index=True,
)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.divider()

import streamlit as st
import pandas as pd

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config = {
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help = "Streamlit **widgets** commands 🎈",
            width = "medium",
            required = True,
        )
    },
    hide_index = True,
    num_rows="dynamic",
)

st.divider()

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area","st.button"],
        "age":["75", "43", "33","67"],
        "gender": ["female", "male", "other", "male"],
        "homepage": ["https://keller-gardner.com/","http://allen-collier.biz/","http://www.schmitt.biz/","https://www.neal.com/"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.TextColumn(
            "Widgets",
            help="Streamlit **widget** commands",
            max_chars=10,
            validate="st\.[a-z]+$",
        )
    },
    hide_index=True,
    num_rows="dynamic",  # For a feature of adding rows
    key="data_editorkey"
)
st.divider()

st.data_editor(data_df, key="data_editor") # 👈 Set a key
st.write("Here's the session state:")
st.write(st.session_state["data_editor"]) # 👈 Access the edited data

st.divider()

import numpy as np

st.data_editor(np.array([
    ["st.text_area", "widget", 4.92],
    ["st.markdown", "element", 47.22]
]))

st.divider()

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

st.divider()

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

st.area_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)

st.divider()

# Initialize session state variables
st.session_state.my_slider = 5
st.session_state.my_checkbox = False

def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key="my_form"):
    slider_input = st.slider('My slider', 0, 10, 5, key = 'myslider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

st.divider()

import streamlit as st

def handle_button_click(arg1, arg2, kwarg1):
    st.write(f"Button clicked with args: {arg1}, {arg2}, and kwarg: {kwarg1}")

# Create a Streamlit button
button_click = st.button("Click me!")

# Check if the button is clicked and call the callback function
if button_click:
    handle_button_click(1, 2, "Hello")


st.divider()

import streamlit as st

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area","st.button"],
        "age":["75", "43", "33","67"],
        "gender": ["female", "male", "other", "male"],
        "homepage": ["https://keller-gardner.com/","http://allen-collier.biz/","http://www.schmitt.biz/","https://www.neal.com/"],
    }
)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(data_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

import streamlit as st

on = st.toggle('Activate feature')

if on:
    st.write('Feature activated!')

import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )

st.write("You selected:", genre)

st.divider()

import streamlit as st
from datetime import datetime

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")

st.write("Start time:", start_time)

st.divider()

import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
if "is_disabled" not in st.session_state:
    st.session_state.is_disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disable_checkbox")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility_radio",  # Unique key for the radio widget
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.is_disabled,
        placeholder=st.session_state.placeholder,
    )

if text_input:
    st.write("You entered: ", text_input)
        
st.divider()

import datetime
import streamlit as st

d = st.date_input("When's your birthday", value=None)
st.write('Your birthday is:', d)

st.divider()

import streamlit as st

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# import streamlit as st

# picture = st.camera_input("Take a picture")

# if picture:
#     st.image(picture)

    st.write("WITHOUT BYTES ----------------------------------------------")

# import streamlit as st
# import pandas as pd

# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     bytes_data = img_file_buffer.getvalue()

#     st.write(type(bytes_data))

#  ---------------------------------------------------------------------------------------

# import streamlit as st

# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # To read image file buffer as bytes:
#     bytes_data = img_file_buffer.getvalue()
#     # Check the type of bytes_data:
#     # Should output: <class 'bytes'>
#     st.divider()
#     # st.write(type(bytes_data))

#  ---------------------------------------------------------------------------------------

# import streamlit as st
# from PIL import Image
# import numpy as np

# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     img = Image.open(img_file_buffer)


#     img_array = np.array(img)


#     st.write(type(img_array))

#     st.write(img_array.shape)

import streamlit as st
import cv2
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:

    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    st.write(type(cv2_img))

    st.write(cv2_img.shape)

st.divider()

import streamlit as st
from PIL import Image

image = Image.open(img_file_buffer)

st.image(image, caption='Sleep rise on the mountain')



# audio.file = st.file_uploader("Choose a audio file", accept_multiple_files=True)

# audio_bytes = audio_file.read() 

# st.audio(audio_bytes, format='audio/ogg')
import streamlit as st

# Upload an audio file
audio_files = st.file_uploader("Choose an audio file", accept_multiple_files=True)

# Check if a file has been uploaded
for audio_file in audio_files:
   # Read the uploaded audio file as bytes
    audio_bytes = audio_file.read()

    # Process the audio_bytes as needed
    # For example, you can play the audio or perform other operations

    # Display some information about the uploaded file
    st.write(f"File Name: {audio_file.name}")
    st.write(f"File Type: {audio_file.type}")
    st.write(f"File Size (bytes): {len(audio_bytes)}")
    st.audio(audio_bytes, format = 'audio/ogg') 

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)

st.write("--------------------------------------------------------------------VIDEO---------------------------------------------------------------------------------------------------")

VIDEO = st.file_uploader("Choose a video file: ", accept_multiple_files = True)

for video_file in VIDEO:
    video_bytes = video_file.read()
    st.video(video_bytes)

import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.sidebar.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
import streamlit as st

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    # with st.spinner("Loading..."):
        # time.sleep(5)  #ERROR
    # st.success("Done!")
# Create a button widget

import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# VIDEO = st.file_uploader("Choose a video file: ", accept_multiple_files = True)

# if VIDEO:
#     for video_file in VIDEO:
#         with tab:
#             video_bytes = video_file.read()
#             st.video(video_bytes)

import streamlit as st

# Generate unique keys for file uploader widgets
video_uploader_1 = st.file_uploader("Choose video file 1: ", accept_multiple_files=True, key="video_uploader_1")
video_uploader_2 = st.file_uploader("Choose video file 2: ", accept_multiple_files=True, key="video_uploader_2")

# Create a list to store uploaded video files
video_files = []

if video_uploader_1:
    video_files.extend(video_uploader_1)

if video_uploader_2:
    video_files.extend(video_uploader_2)

# Create a dropdown to select the video to display
selected_video = st.selectbox("Choose a video:", [f"Video {i+1}" for i in range(len(video_files))])

# Display the selected video
if video_files:
    selected_index = int(selected_video.split()[-1]) - 1
    selected_video_bytes = video_files[selected_index].read()
    st.video(selected_video_bytes)

import streamlit as st
import time

with st.empty():
    for seconds in range(5):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 10 seconds!")

import streamlit as st

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')

if st.button('Click me'):
    st.write('You clicked the button!')
    # st.rerun()