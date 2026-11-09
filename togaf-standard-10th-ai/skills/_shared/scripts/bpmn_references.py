"""Resolve same-document BPMN IDs without aliasing external QName namespaces.

BPMN 2.0.2 section 15.3.2 defines the local part as the referenced ID.
Unprefixed references retain the standard's same-document ID convention.
External or undeclared prefixes remain unresolved and are never fetched.
"""
def local_id(value):
    """Consume XML Schema ID/IDREF whitespace collapse for one identity token."""
    return value.strip() if value is not None else None


def local_reference(owner, value, target_namespace):
    if not value or not value.strip():
        return None, None
    value = value.strip()
    if ':' not in value:
        return value, None
    prefix, identity = value.split(':', 1)
    if not identity or ':' in identity or not target_namespace or owner.nsmap.get(prefix) != target_namespace:
        return None, 'external QName binding unresolved: ' + value
    return identity, None
