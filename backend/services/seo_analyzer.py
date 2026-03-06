import re

class SEOAnalyzer:
    def __init__(self):
        self.score = 0
        self.issues = []

    def analyze(self, url, meta_tags):
        self.score = 100
        self.issues = []
        self._check_title(meta_tags.get('title', ''))
        self._check_description(meta_tags.get('description', ''))
        self._check_og_tags(meta_tags)
        return {
            'url': url,
            'score': self.score,
            'issues': self.issues,
            'meta_tags': meta_tags
        }

    def _check_title(self, title):
        if not title:
            self.issues.append({'type': 'title', 'message': 'Missing title tag', 'severity': 'critical'});
            self.score -= 20;
        elif len(title) < 10 or len(title) > 60:
            self.issues.append({'type': 'title', 'message': 'Title should be 10-60 chars', 'severity': 'warning'});
            self.score -= 10;

    def _check_description(self, desc):
        if not desc:
            self.issues.append({'type': 'description', 'message': 'Missing meta description', 'severity': 'critical'});
            self.score -= 20;
        elif len(desc) < 50 or len(desc) > 160:
            self.issues.append({'type': 'description', 'message': 'Description should be 50-160 chars', 'severity': 'warning'});
            self.score -= 10;

    def _check_og_tags(self, meta_tags):
        required = ['og:title', 'og:description', 'og:image']
        for tag in required:
            if not meta_tags.get(tag):
                self.issues.append({'type': 'og_tags', 'message': f'Missing {tag}', 'severity': 'warning'});
                self.score -= 5
