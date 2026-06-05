import plotly.express as px


def create_pie_chart(data, title):

    fig = px.pie(
        values=data.values,
        names=data.index,
        title=title,
        hole=0.4
    )

    return fig


def create_bar_chart(data, title):

    fig = px.bar(
        x=data.index,
        y=data.values,
        title=title
    )

    return fig


def create_line_chart(x, y, title):

    fig = px.line(
        x=x,
        y=y,
        title=title,
        markers=True
    )

    return fig


def create_histogram(df, column, title):

    fig = px.histogram(
        df,
        x=column,
        title=title
    )

    return fig