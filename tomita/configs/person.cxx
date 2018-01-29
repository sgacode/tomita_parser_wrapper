#encoding "utf8"

PersonName -> Word<kwtype="имя">;
PersonName -> Word<kwtype="имя"> (Word<h-reg1>);

Person -> PersonName interp (Person.Name);