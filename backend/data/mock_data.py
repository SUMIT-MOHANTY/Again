from backend.models import db, Portfolio, Category, Technology

MOCK_CATEGORIES = ['Web Development', 'Mobile App', 'Data Science', 'DevOps']
MOCK_TECHNOLOGIES = ['React', 'Python', 'TypeScript', 'PostgreSQL', 'Docker', 'AWS', 'Node.js', 'Vue.js']

MOCK_PORTFOLIOS = [
    {'title': 'E-Commerce Platform', 'description': 'Full-stack e-commerce solution with payment integration', 'category': 'Web Development', 'technologies': ['React', 'Node.js', 'PostgreSQL'], 'image_url': 'https://via.placeholder.com/300', 'project_url': 'https://example.com'},
    {'title': 'Task Management App', 'description': 'Collaborative task management with real-time updates', 'category': 'Mobile App', 'technologies': ['React', 'TypeScript', 'AWS'], 'image_url': 'https://via.placeholder.com/300', 'project_url': 'https://example.com'},
    {'title': 'ML Pipeline', 'description': 'Automated machine learning pipeline for data processing', 'category': 'Data Science', 'technologies': ['Python', 'AWS', 'Docker'], 'image_url': 'https://via.placeholder.com/300', 'project_url': 'https://example.com'},
    {'title': 'CI/CD System', 'description': 'Continuous integration and deployment infrastructure', 'category': 'DevOps', 'technologies': ['Docker', 'AWS', 'Python'], 'image_url': 'https://via.placeholder.com/300', 'project_url': 'https://example.com'},
    {'title': 'Portfolio Website', 'description': 'Personal portfolio with blog and contact form', 'category': 'Web Development', 'technologies': ['Vue.js', 'TypeScript', 'PostgreSQL'], 'image_url': 'https://via.placeholder.com/300', 'project_url': 'https://example.com'},
    {'title': 'Weather Dashboard', 'description': 'Real-time weather monitoring and forecasting', 'category': 'Web Development', 'technologies': ['React', 'Python', 'AWS'], 'image_url': 'https://via.placeholder.com/300', 'project_url': 'https://example.com'},
    {'title': 'Fitness Tracker', 'description': 'Mobile app for tracking workouts and nutrition', 'category': 'Mobile App', 'technologies': ['React', 'Node.js', 'PostgreSQL'], 'image_url': 'https://via.placeholder.com/300', 'project_url': 'https://example.com'},
    {'title': 'Analytics Dashboard', 'description': 'Business intelligence dashboard with visualizations', 'category': 'Data Science', 'technologies': ['Python', 'TypeScript', 'PostgreSQL'], 'image_url': 'https://via.placeholder.com/300', 'project_url': 'https://example.com'},
    {'title': 'Kubernetes Cluster', 'description': 'Managed Kubernetes cluster for microservices', 'category': 'DevOps', 'technologies': ['Docker', 'AWS', 'Python'], 'image_url': 'https://via.placeholder.com/300', 'project_url': 'https://example.com'},
    {'title': 'Social Media App', 'description': 'Social networking platform with real-time chat', 'category': 'Mobile App', 'technologies': ['React', 'Node.js', 'AWS'], 'image_url': 'https://via.placeholder.com/300', 'project_url': 'https://example.com'},
]

def load_mock_data():
    if Category.query.first():
        return
    categories = {name: Category(name=name) for name in MOCK_CATEGORIES}
    technologies = {name: Technology(name=name) for name in MOCK_TECHNOLOGIES}
    db.session.add_all(list(categories.values()) + list(technologies.values()))
    db.session.commit()
    for p in MOCK_PORTFOLIOS:
        portfolio = Portfolio(
            title=p['title'],
            description=p['description'],
            category=categories[p['category']],
            image_url=p['image_url'],
            project_url=p['project_url']
        )
        portfolio.technologies = [technologies[t] for t in p['technologies'] if t in technologies]
        db.session.add(portfolio)
    db.session.commit()
