# HTML img tag convert script

## About

It replaces img tag to Rails's url helper method.

`<img src="/img/hoge.png" alt="It's hoge"`>
->
`<%= image_tag("hoge.png", alt: "It's hoge") %>`

## How to use

