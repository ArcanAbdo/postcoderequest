from app_code.postcode_class import PostCode
from pprint import pprint

a = PostCode("B14 7EG")

pprint(a.check_length())
pprint(a.output_full())
pprint(a.output_location())
