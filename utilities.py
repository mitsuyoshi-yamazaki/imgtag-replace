#!/usr/bin/python

import os, re, functools

def find(pattern, string):
  result = re.findall(pattern, string)
  if len(result) == 0:
    return None
  return result[0]
setattr(re, 'find', find)

def has(pattern, string):
  return re.find(pattern, string) is not None
setattr(re, 'has', has)

def listfile(path):
  from os.path import isfile, join
  import operator
  getfiles = lambda x: [x] if isfile(x) else listfile(x)
  files = [getfiles(join(path, o)) for o in os.listdir(path)]
  return functools.reduce(operator.add, files)

def check_attributes(attributes, tag):
  check = tag
  for key in attributes:
    attr = re.find('%s=".*?"' % key, tag)
    check = check.replace(attr, '')
  check = check.replace('<img', '')
  check = check.replace('/>', '')
  check = check.replace('>', '')
  check = check.replace(' ', '')
  if len(check) > 0:
    print('tag has unexpected attributes: %s\n%s\n%s' % (attributes, check, tag))
    raise Exception('unexpected attributes')

def get_attributes(tag):
  keys = re.findall(' ([\w-]+?)=', tag)
  result = {}
  for key in keys:
    value = re.find('%s="(.*?)"' % key, tag)
    if value is None:
      print('cannot find attribute "%s" in %s' % (key, tag))
      continue
    result[key] = value
  check_attributes(keys, tag)
  return result

def replace_file(filepaths, replace_image_tag):
  for path in filepaths:
    with open(path, 'r+') as f:
      html = f.read()
      f.seek(0)
      html = replace_image_tag(html, path)
      f.write(html)
      f.truncate()
