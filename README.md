# python-demo

CREATE TABLE `aws_collection` 
(  id varchar(20),
  `title` text COLLATE utf8_bin DEFAULT NULL,
  `url` varchar(2000) COLLATE utf8_bin DEFAULT NULL,
  `comment_count` int(11) DEFAULT NULL,
  `score` varchar(20) COLLATE utf8_bin DEFAULT NULL,
   page int,
   indexseq int,
   type varchar(20),
   keyword varchar(400)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE `aws_collection_statis` (
  `word` varchar(2000) COLLATE utf8_bin DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL,
  `num` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


CREATE TABLE `aws_collection_content` (
  `id` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `content` text COLLATE utf8_bin
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


https://blog.csdn.net/lcr_happy/article/details/73252819