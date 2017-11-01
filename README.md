# HTML img tag convert script

## About

It replaces img tag to Rails's url helper method.

`<img src="/img/hoge.png" alt="It's hoge"`>
->
`<%= image_tag("hoge.png", alt: "It's hoge") %>`

## How to use

```shell
$ ./replace.py path/to/directory/containing/htmls
$ ./replace.py path/to/directory/containing/htmls --dry_run
```

The script recursively search in the given directory and collect files with `.html.erb` extension.

`--dry_run` option must be given as THIRD argument, otherwise the script doesn't recognize.
May fix it to sane implement in the future.

Output `image path not found in tag:` suggests that the script found a img tag but it can't find an image path in it, so skips replacing.