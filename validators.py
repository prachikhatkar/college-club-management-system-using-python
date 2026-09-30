def valid_text(v): return bool(v.strip())
def valid_id(v): return bool(v.strip())
def valid_date(v):
 p=v.split("-"); return len(p)==3 and all(x.isdigit() for x in p)
