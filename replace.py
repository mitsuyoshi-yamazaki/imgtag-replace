#!/usr/bin/python

import sys
from utilities import *

print("replace image tags")
print("arguments: %s" % sys.argv)

dirpath = sys.argv[1]
print("path: %s" % dirpath)

is_dry = False
if len(sys.argv) >= 3:
  if sys.argv[2] == '--dry_run': # forgive me
    is_dry = True
  else:
    raise Exception('unexpected option "%s"' % sys.argv[2])

imagepaths = []

def replace_image_tag(html, path=None):
  tags = re.findall('<img.+?src="/img.+?>', html)
  for tag in tags:
    image = re.find('src="/img/(.+?)"', tag)
    if image is None:
      print('image path not found in tag: "%s" in %s' % (tag, path))
      continue
    imagepaths.append(image)
    attributes = get_attributes(tag)
    attributes.pop('src')
    if len(attributes) > 0:
      # http://railsdoc.com/references/image_tag
      # <img src="/img/hoge.png" alt="hogera"> -> <%= image_tag("hoge.png", alt: "hogera") %>
      attributes = ', '.join(['%s: "%s"' % o for o in attributes.items()])
      replaced = '<%%= image_tag("%s", %s) %%>' % (image, attributes)
    else:
      replaced = '<%%= image_tag("%s") %%>' % (image)
    if is_dry:
      print('"%s" -> "%s"' % (tag, replaced))
      continue
    html = html.replace(tag, replaced)
  return html

filepaths = listfile(dirpath)
html_filepaths = [f for f in filepaths if f.endswith('.html.erb')]
replace_file(html_filepaths, replace_image_tag)
