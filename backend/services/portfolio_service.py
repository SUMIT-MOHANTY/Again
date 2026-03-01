from backend.models import Portfolio

def search_portfolios(query: str, category: str, tags: list) -> list:
    q = Portfolio.query
    if query:
        q = q.filter(
            (Portfolio.title.ilike(f'%{query}%')) |
            (Portfolio.description.ilike(f'%{query}%'))
        )
    if category:
        q = q.join(Portfolio.category).filter(Portfolio.category.has(name=category))
    if tags:
        from backend.models import portfolio_tech, Technology
        q = q.join(portfolio_tech).join(Technology).filter(Technology.name.in_(tags))
    return q.all()
