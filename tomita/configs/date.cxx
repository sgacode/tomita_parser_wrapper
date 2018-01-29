#encoding "utf-8"

DayOfWeek -> Noun<kwtype="день_недели">;      // используем слова из статьи "день_недели"
Day -> AnyWord<wff=/([1-2]?[0-9])|(3[0-1])/>; // число от 1 до 31

Month -> Noun<kwtype="месяц">;                // используем слова из статьи "месяц"
Month -> AnyWord<wff=/(0?[1-9])|(1[0-2])/>;   // число от 1 до 12

YearDescr -> "год" | "г. ";
Year -> AnyWord<wff=/[1-2]?[0-9]{1,3}г?\.?/>; // число от 0 до 2999 с возможным "г" или "г." в конце
Year -> Year YearDescr;

        // день недели, запятая, число, месяц и год:
        // "понедельник, 3 сентября 2012г."
Date -> DayOfWeek interp (Date.DayOfWeek) (Comma)
        Day interp (Date.Day)
        Month interp (Date.Month)
        (Year interp (Date.Year));

        // число, месяц и год: "10 января 2011" | "10.01.2011"
Date -> Day interp (Date.Day)(Punct)
        Month interp (Date.Month)(Punct)
        (Year interp (Date.Year));

        // число, месяц и год: "2011 январь 10" | "2011.10.01"
Date -> (Year interp (Date.Year))(Punct)
        Month interp (Date.Month)(Punct)
        Day interp (Date.Day);

        // месяц и год: "июнь 2009"
Date -> Month interp (Date.Month)
        Year interp (Date.Year);