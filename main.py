from dash import Dash 
import dash_bootstrap_components as dbc
import i18n
from layout import create_layout

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"


LOCALE = "ru"

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}
def main():
    i18n.set("locale", LOCALE)
    i18n.load_path.append("locale")

    app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY, dbc_css])
    app.title = i18n.t("labels.title")
    app.layout = create_layout(app)
    app.run(debug=True)

if __name__ == '__main__':
    main()