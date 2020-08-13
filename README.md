# translation_API

Flask and Google translation based API.  

XML is used to request and response.



## End points

- /translate/to_en
- /translate/to_ja



## Sample XML

- Request

```xml
<?xml version="1.0" encoding="utf-8"?>
<request>
  <text>
    Hello, I like sleeping
  </text>
</request>
```



- Response

```xml
<?xml version="1.0" encoding="utf-8"?>
<response>
  <text>
    こんにちは、寝るのが好きです
  </text>
  <error_message>
  </error_message>
  <status>
  	0
  </status>
</response>
```



## How to run

```shell
$ cd translation_API
$ docker-compose up
```

