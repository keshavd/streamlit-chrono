# streamlit-chrono

Streamlit port of the react-chrono library. Allows for the rendering of timelines with cards.

## Installation instructions

```sh
pip install streamlit-chrono
```

## Usage instructions

The `streamlit_chrono` API is similar to `react-chrono` interface.

See the documentation at https://github.com/prabhuignoto/react-chrono

```python
import streamlit as st
import json
from streamlit_chrono import chrono

items=[
    {"title": "Home"},
    {"title": "Workflow"},
    {"title": "Diagnostic Features"},
    {"title": "Referential Groups"},
    {"title": "Review Changes"},
    {"title": "Run Workflow"},
]
active_item_index=0

current_item = chrono(
    items=items,
    active_item_index=active_item_index
)

st.write(json.dumps(current_item, indent=4))
```