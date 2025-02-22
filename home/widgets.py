from django.forms.widgets import CheckboxSelectMultiple
from django.utils.html import format_html, format_html_join
from django.utils.encoding import force_str

class CustomCheckboxSelectMultiple(CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = []
        final_attrs = self.build_attrs(attrs)
        output = []
        # Normalize to strings.
        str_values = set([force_str(v) for v in value])
        # Build options manually.
        for i, (option_value, option_label) in enumerate(self.choices):
            option_value = force_str(option_value)
            checkbox_id = f'{final_attrs.get("id", name)}_{i}'
            final_attrs_option = final_attrs.copy()
            final_attrs_option['id'] = checkbox_id
            checked = ' checked' if option_value in str_values else ''
            output.append(
                format_html(
                    '<label class="custom-checkbox"><input type="checkbox" name="{}" value="{}" id="{}"{}> <span class="checkbox-label">{}</span></label>',
                    name, option_value, checkbox_id, checked, option_label
                )
            )
        return format_html_join('\n', '{}', ((item,) for item in output))
