class AccessibilityValidator:
    WCAG_RULES = {
        'img_alt': {'impact': 'critical', 'description': 'Images must have alt text'},
        'heading_order': {'impact': 'serious', 'description': 'Heading levels should not be skipped'},
        'link_name': {'impact': 'critical', 'description': 'Links must have discernible text'},
        'button_name': {'impact': 'critical', 'description': 'Buttons must have discernible text'},
        'color_contrast': {'impact': 'serious', 'description': 'Sufficient color contrast required'},
    }

    def check_wcag(self, url, html_content):
        violations = []
        score = 100

        # Simulated validation
        if '<img' in html_content and 'alt=' not in html_content:
            violations.append({'rule': 'img_alt', 'impact': 'critical', 'nodes': 1});
            score -= 15

        if '<h1' in html_content and '<h2' in html_content:
            violations.append({'rule': 'heading_order', 'impact': 'serious', 'nodes': 1});
            score -= 10

        return {
            'url': url,
            'wcag_level': 'AA',
            'score': max(0, score),
            'violations': violations,
            'recommendations': ['Add alt text to all images', 'Ensure proper heading hierarchy', 'Add aria-labels to interactive elements']
        }
