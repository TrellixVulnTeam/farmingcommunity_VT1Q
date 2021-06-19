from .. import Provider as AddressProvider


class Provider(AddressProvider):
    city_formats = ['{{city_name}}']
    street_name_formats = ['{{street_title}} {{street_suffix}}']
    street_address_formats = ['{{street_name}} {{building_number}}']
    address_formats = ['{{street_address}}, {{city}}']
    building_number_formats = ['##']
    street_suffixes = ['ქ.']

    # Source: Wikipedia's list of sovereign states
    # https://en.wikipedia.org/wiki/List_of_sovereign_states
    countries = (
        'ავსტრალია', 'ავსტრია', 'ავღანეთი', 'აზერბაიჯანი', 'ალბანეთი', 'ალჟირი',
        'ამერიკის სამოა', 'ამერიკის ვირჯინიის კუნძულები',
        'ამერიკის შეერთებული შტატები', 'ანგილია', 'ანგოლა', 'ანდორა',
        'ანტიგუა და ბარბუდა', 'არაბთა გაერთიანებული საამიროები', 'არგენტინა',
        'არუბა', 'აღმოსავლეთი ტიმორი', 'ახალი ზელანდია', 'ახალი კალედონია',
        'ბანგლადეში', 'ბარბადოსი', 'ბასას-და-ინდია', 'ბაჰამის კუნძულები',
        'ბაჰრეინი', 'ბელარუსი', 'ბელგია', 'ბელიზი', 'ბენინი', 'ბერმუდა',
        'ბოლივია', 'ბოსნია და ჰერცეგოვინა', 'ბოტსვანა', 'ბრაზილია',
        'ბრიტანეთის ვირჯინიის კუნძულები',
        'ბრიტანეთის ინდოეთის ოკეანის ტერიტორია', 'ბრუნეი', 'ბულგარეთი',
        'ბურკინა ფასო', 'ბურუნდი', 'ბუვე', 'ბჰუტანი', 'გაბონი', 'გაიანა',
        'გამბია', 'განა', 'გერმანია', 'გვადელუპა', 'გვატემალა', 'გვინეა',
        'გვინეა-ბისაუ', 'გიბრალტარი', 'გრენადა', 'გრენლანდია', 'გუამი', 'დანია',
        'დიდი ბრიტანეთი', 'დომინიკელთა რესპუბლიკა', 'დომინიკა', 'ეგვიპტე',
        'ევროპა (კუნძული)', 'ეთიოპია', 'ეკვადორი', 'ეკვატორული გვინეა', 'ერაყი',
        'ერიტრეა', 'ესპანეთი', 'ესტონეთი', 'ეშმორის და კარტიეს კუნძულები',
        'უოლისი და ფუტუნა', 'ვანუატუ', 'ვატიკანი', 'ვენესუელა', 'ვიეტნამი',
        'ზამბია', 'ზიმბაბვე', 'თურქეთი', 'თურქმენეთი', 'იამაიკა', 'იან მაიენი',
        'იაპონია', 'იემენი', 'ინდოეთი', 'ინდონეზია', 'იორდანია', 'ირანი',
        'ირლანდია', 'ისლანდია', 'ისრაელი', 'იტალია', 'კაბო-ვერდე',
        'კაიმანის კუნძულები', 'კამბოჯა', 'კამერუნი', 'კანადა', 'კატარი',
        'კენია', 'კვიპროსი', 'კინგმენის რიფი', 'კირიბატი', 'ქოქოსის კუნძულები',
        'კოლუმბია', 'კომორის კუნძულები', 'კონგოს დემოკრატიული რესპუბლიკა',
        'კონგოს რესპუბლიკა', 'კორეის რესპუბლიკა', 'ჩრდილოეთი კორეა',
        'კოსტა-რიკა', 'კოტ-დ’ივუარი', 'კუბა', 'კუკის კუნძულები', 'ლაოსი',
        'ლატვია', 'ლესოთო', 'ლიბანი', 'ლიბერია', 'ლიბია', 'ლიტვა',
        'ლიხტენშტაინი', 'ლუქსემბურგი', 'მადაგასკარი', 'მავრიკი', 'მავრიტანია',
        'მაიოტა', 'მაკაო', 'მაკედონია', 'მალავი', 'მალაიზია', 'მალდივი', 'მალი',
        'მალტა', 'მაროკო', 'მარშალის კუნძულები', 'მარჯნის ზღვის კუნძულები',
        'მექსიკა', 'მიანმარი', 'მიკრონეზია', 'მოზამბიკი', 'მოლდოვა', 'მონაკო',
        'მონსერატი', 'მონღოლეთი', 'ნამიბია', 'ნაურუ', 'ნეპალი', 'ნიგერი',
        'ნიგერია', 'ნიდერლანდი', 'ნიდერლანდის ანტილები', 'ნიკარაგუა', 'ნიუე',
        'ნორვეგია', 'ნორფოლკის კუნძული', 'ომანი', 'პაკისტანი', 'პალაუ',
        'პალმირა (ატოლი)', 'პანამა', 'პაპუა-ახალი გვინეა', 'პარაგვაი', 'პერუ',
        'პიტკერნის კუნძულები', 'პოლონეთი', 'პორტუგალია',
        'პრინც-ედუარდის კუნძული', 'პუერტო-რიკო', 'ჟუან-დი-ნოვა', 'რეიუნიონი',
        'რუანდა', 'რუმინეთი', 'რუსეთი', 'საბერძნეთი', 'სალვადორი', 'სამოა',
        'სამხრეთ აფრიკის რესპუბლიკა',
        'სამხრეთი გეორგია და სამხრეთ სენდვიჩის კუნძულები', 'სამხრეთი სუდანი',
        'სან-მარინო', 'სან-ტომე და პრინსიპი', 'საუდის არაბეთი', 'საფრანგეთი',
        'საფრანგეთის გვიანა', 'საფრანგეთის პოლინეზია',
        'საფრანგეთის სამხრეთული და ანტარქტიდული ტერიტორია', 'საქართველო',
        'სეიშელის კუნძულები', 'სენეგალი', 'სენ-პიერი და მიკელონი',
        'სენტ-ვინსენტი და გრენადინები', 'სენტ-კიტსი და ნევისი', 'სენტ-ლუსია',
        'სერბეთი', 'სეუტა', 'სვაზილენდი', 'სვალბარდი', 'სიერა-ლეონე',
        'სინგაპური', 'სირია', 'სლოვაკეთი', 'სლოვენია', 'სოლომონის კუნძულები',
        'სომალი', 'სომხეთი', 'სუდანი', 'სურინამი', 'ტაივანი', 'ტაილანდი',
        'ტანზანია', 'ტაჯიკეთი', 'ტერქსისა და კაიკოსის კუნძულები', 'ტოგო',
        'ტოკელაუ', 'ტონგა', 'ტრინიდადი და ტობაგო', 'ტუვალუ', 'ტუნისი', 'უგანდა',
        'უზბეკეთი', 'უკრაინა', 'უნგრეთი', 'ურუგვაი', 'ფარერის კუნძულები',
        'ფილიპინები', 'ფინეთი', 'ფიჯი', 'ფოლკლენდის კუნძულები', 'ქუვეითი',
        'ღაზის სექტორი', 'ყაზახეთი', 'ყირგიზეთი', 'შვეიცარია', 'შვედეთი',
        'შობის კუნძული', 'შრი-ლანკა', 'ჩადი', 'ჩერნოგორია', 'ჩეხეთი',
        'ჩეჩნეთის რესპუბლიკა იჩქერია', 'ჩილე', 'ჩინეთი',
        'ჩრდილოეთი მარიანას კუნძულები', 'ცენტრალური აფრიკის რესპუბლიკა',
        'წმინდა ელენე, ამაღლება და ტრისტანი-და-კუნია',
        'წყნარი ოკეანის კუნძულები', 'ხორვატია', 'ჯერსი', 'ჯიბუტი', 'ჰაიტი',
        'ჰონდურასი', 'ჰონკონგი', 'ჰერდი და მაკდონალდის კუნძულები',
    )

    # Source: Tbilisi city directory
    # http://directory.ge/map/index.php?lang=eng
    street_titles = (
        '300 არაგველის', '8 მარტის', 'აბაკელიას', 'აბანოს', 'აბასთუმანის',
        'აბაშელის', 'აბაშის', 'აბაშიძე გრიგოლის', 'აბაშიძე დოდოს',
        'აბაშიძე ირაკლის', 'აბაშიძე ჰეიდარის', 'აბაშიძის',
        'აბდუშელიშვილი მალხაზის', 'აბესაძე გიას', 'აბზიანიძის', 'აბო ტბილელის',
        'აბოვიანის', 'აბუსერიძე-ტბელის', 'აგარის', 'აგლაძე რაფიელის',
        'ადიგენის', 'ავთანდილის', 'ავლაბრის', 'ავლევის', 'ათონელის', 'აკეთის',
        'აკოფიანის', 'აკურის', 'ალადაშვილის', 'ალაზნის', 'ალგეთის',
        'ალექსიძე მერაბის', 'ალვანის', 'ალიხანიანის', 'ალმასიანის', 'ამაღლების',
        'ამბროლაურის', 'ამირანაშვილი პეტრეს', 'ამირეჯიბის', 'ანაკლიის',
        'ანანურის', 'ანდრონიკაშვილის', 'ანდღულაძის', 'ანტონ კატალიკოსის',
        'ანტონოვსკაიას', 'ანჯაფარიძე ვერიკოს', 'არაგვის', 'არაგვისპირელი შიოს',
        'არალეთის', 'არარატის', 'არაყიშვილი დიმიტრის', 'არბოს', 'არბოშიკის',
        'არგვეთის', 'არდაზიანის', 'არდონის', 'არეშიძის', 'არველაძის',
        'ართვინის', 'არმაზის', 'არსენალის', 'ასათიანი ლადოს', 'ასკანის',
        'ასურეთის', 'ასხინის', 'ატენის', 'აფანასიევის', 'აფხაზეთის', 'აწყურის',
        'აჭარის', 'ახალარსენალის', 'ახალდაბის', 'ახალუბნის', 'ახალქალაქის',
        'ახვლედიანი ელენეს', 'ახვლედიანი გიორგის', 'ახვლედიანის', 'ახმეტელის',
        'ახმეტის', 'ახოსპირელის', 'ახტალის', 'ახუთის', 'ახუნდოვის', 'აჯამეთის',
        'ბააზოვის', 'ბაგინეთის', 'ბადიაურის', 'ბაზალეთის', 'ბათუმის',
        'ბაკურიანის', 'ბაკურციხის', 'ბალადინის', 'ბალანჩივაძე მელიტონის',
        'ბარათაშვილი ნოკოლოზის', 'ბარათაშვილის', 'ბარალეთის',
        'ბარამიძე ალექსანდრეს', 'ბარისახოს', 'ბარნოვის', 'ბაქოს',
        'ბაქრაძე დავითის', 'ბაქრაძე დიმიტრის', 'ბაღდათის', 'ბაღნარის',
        'ბახმაროს', 'ბახტრიონის', 'ბედიის', 'ბევრეთის', 'ბეთანიის', 'ბეთლემის',
        'ბელიაშვილი აკაკის', 'ბენაშვილის', 'ბენდელიანი ჭიჭიკოს',
        'ბეჟანიშვილი ეკას', 'ბერბუქის', 'ბერიაშვილის', 'ბერიკაშვილის',
        'ბერიტაშვილის', 'ბერიძე ვუკოლის', 'ბერძენიშვილის', 'ბესიკის',
        'ბექა ოპიზარის', 'ბეღლეთის', 'ბზიფის', 'ბიჭვინთის', 'ბოგვის', 'ბოდავის',
        'ბოდბის', 'ბოლნისის', 'ბორბალოს', 'ბოროდინოს', 'მ. ლებანიძის',
        'ბოტანიკურის', 'ბოცვაძის', 'ბოჭორიშვილის', 'ბოჭორმის', 'ბჟოლეთის',
        'ბროლოსანის', 'ბროსეს', 'ბუაჩიძე თენგიზის', 'ბუდაპეშტის', 'ბულაჩაურის',
        'ბურკიაშვილის', 'ბურძგლას', 'ბუღეულის', 'ბუხაიძის',
        'გაბაშვილი ეკატერინეს', 'გაგარინი იურის', 'გალავნის',
        'გალაქტიონ ტაბიძის', 'გალის', 'გამრეკელის', 'გამყრელიძის',
        'გამცემლიძე შოთას', 'განთიადის', 'გარე კახეთის', 'გარეჯელი დავითის',
        'გარიყული მარიამის', 'გაფრინდაულის', 'გახოკიძე აკაკის', 'გახოკიძის',
        'გეგუთის', 'გედევანიშვილის', 'გეზათის', 'გელათის', 'გერგეტის',
        'გვაზაურის', 'გვეტაძე რაჟდენის', 'გივიშვილის', 'გიორგაძის',
        'გიორგი ბრწყინვალის', 'გიორგი მერჩულეს', 'გლინკას', 'გოგაშენის',
        'გოგებაშვილის იაკობის', 'გოგიბერიძის', 'გოგოლაურის', 'გოგოლის',
        'გოგჩის', 'გოთუას', 'გოკიელის', 'გომარეთის', 'გომბორის', 'გომის',
        'გონაშვილი ჰამლეტის', 'გორგასლის', 'გორდის', 'გორის', 'გორკის',
        'გოცირიძის', 'გოძიაშვილის', 'გრანელი ტერენტის', 'გრიბოედოვის',
        'გრიშაშვილის', 'გროზნოს', 'გრუზინსკი პეტრეს', 'გუდამაყრის', 'გუდარეხის',
        'გუდარის', 'გუდაუთის', 'გუდიაშვილი ლადოს', 'გუთნის', 'გულიას',
        'გულისაშვილის', 'გულუა გიას', 'გუმათის', 'გუმათჰესის', 'გუმბრის',
        'გუნიას', 'გურგენიძის', 'გურიელის', 'გურიის', 'გურჯაანის', 'დაბახანას',
        'დადიანი შალვას', 'დადიანი ცოტნეს', 'დაისის', 'ლ. ელიავას', 'დარკვეთის',
        'დგებუაძის', 'დედოფლისწყაროს', 'დეკაბრისტების', 'დელისის', 'დეპოს',
        'დვალის', 'დვირის', 'დიდგორის', 'დიდხევის', 'დიდი ხეივნის',
        'დიდი ჯიხაიშის', 'დ. ყიფიანის', 'დიმიტრი თავდადებულის', 'დირსიჭალას',
        'დიუმა ალექსანდრეს', 'დმანისის', 'დობროლიუბოვის', 'დოდაშვილი სოლომონის',
        'დოესის', 'დოლიძე გოგის', 'დოლიძის', 'დოქის', 'დოღუმბარის',
        'დუტუ მეგრელის', 'დუშეთის', 'ედისის', 'ევდოშვილის', 'ეკალაძის',
        'ელდარის', 'ენგურის', 'ენგურჰესის', 'ენისელის', 'ენუქიძის', 'ერევნის',
        'ერისთავი თორნიკეს', 'ერისთავი კონსტანტინეს', 'ერისთავ-ხოშტარიას',
        'ერწოს', 'ესენინის', 'სანდრო ეულის', 'ეფრემ მცირის', 'ექიმის',
        'ვაზიანის', 'ვაზისუბნის', 'ვაკელი იონას', 'ვანის', 'ვარდევანის',
        'ვარდისუბნის', 'ვართაგავას', 'რომის', 'ვასაძის', 'ვაშლოვანის',
        'ვახტანგ VI–ის', 'ვეზიროვის', 'ვეკუა ვოვას', 'ვერცხლის', 'ვერჰარნის',
        'ვეძათხევის', 'ვეძინის', 'ვირსალაძის', 'ვორონინის', 'საარბრჯუკენის',
        'ზაზიშვილი გიგოს', 'ზალდასტანიშვილის', 'ზანდუკელი მიხეილის', 'ზარზმის',
        'ზაქარიაძე სერგოს', 'ზედაზნის', 'ზედამზის', 'ზედაუბნის', 'ზეინკლის',
        'ზეკარის', 'ზემო ვაკის', 'ზემო ვეძისის', 'ზესტაფონის', 'ზვარეთის',
        'ზიარის', 'ზიგზაგის', 'ზინდისის', 'ზიჩი მიხაის', 'ზოვრეთის',
        'ზუბალაშვილების', 'ზუგდიდის', 'ზურაბიშვილი ავლიპის',
        'თაბუკაშვილი რეზოს', 'თავაძე ფერდინანდის', 'თამარაშენის',
        'თამარაშვილი მიხეილის', 'გ. სვანიძის', 'თარხნიშვილის', 'თაქთაქიშვილის',
        'თაყაიშვილი სესილიას', 'თევდორე მღვდლის', 'თეთნულდის', 'თეთრიწყაროს',
        'თეკლათის', 'თელავის', 'ხახანაშვილის', 'თელეთის', 'თერგის', 'თეძმის',
        'თვალჭრელიძის', 'თიანეთის', 'თმოგველის', 'თმოგვის', 'თოდრიას', 'თოიძის',
        'თონეს', 'თორაძის', 'თოფურიას', 'თრიალეთის', 'თუმანიანის', 'თხინვალის',
        'იალბუზის', 'იამანიძე შოთას', 'იაშვილი პაოლოს', 'იბრაჰიმ ისპაჰანელის',
        'იდუმალას', 'იეთიმ გურჯის', 'იერუსალიმის', 'ივერიის', 'ივლეთის',
        'იზაშვილის', 'ილორის', 'ილურიძე კონსტანტინეს', 'იმედაშვილი გაიოზის',
        'იმერეთის', 'ინანიშვილი რამაზის', 'ინაშვილის', 'ინგოროყვა პავლეს',
        'ინტერნატის', 'იორის', 'იოსებიძის', 'იოსელიანის', 'იპოლიტე-ივანოვის',
        'ირბაქი ნიკიფორეს', 'ირგვლივის', 'ისაკიანის', 'ისნის', 'იფნის',
        'იყალთოს', 'კავთისხევის', 'კავსაძის', 'კაიშაურის',
        'კაკაბაძე პოლიკარპეს', 'კაკაბაძეების', 'კაკლიანის', 'კოტე ხიმშიაშვილის',
        'კალატოზის', 'კალიუჟნის', 'კალოუბნის', 'კანდელაკის', 'კანდელაკის',
        'კანკავას', 'კაპანაძის', 'კარალეთის', 'კარგარეთელის', 'კასპის',
        'კაჭრეთის', 'კახიანის', 'კედია სპირიდონის', 'კეკელიძე კორნელის',
        'კელაპტრიშვილი ომარის', 'კერესელიძე არჩილის', 'კერესელიძის',
        'კეცხოველი ნიკოს', 'კვალეთის', 'კვალის', 'კვანტალიანის', 'კვერნაულის',
        'კვესეთის', 'კიევის', 'კიკეთის', 'კიკვიძის', 'კისისხევის', 'კიშინიოვის',
        'კლდეკარის', 'კლდიაშვილის', 'კნოლევის', 'კობახიძის', 'კობერიძის',
        'კოდალოს', 'კოდორის', 'კოკინაკის', 'კოლმეურნეობის ველის', 'კოლხეთის',
        'კომუნის', 'კონდოლის', 'კონსტიტუციის', 'კოფცოვის', 'კოსტავას',
        'კოტეტიშვილი ვახტანგის', 'კოშკოვანის', 'კოხრეიძის', 'კოჯრის',
        'ჯ. კახიძის', 'კრწანისის', 'კუმისის', 'კუპრაძის', 'კურნატოვსკის',
        'კურსების', 'კურსკის', 'კუფტინის', 'ლაგოდეხის', 'ლაზოს', 'ლაითურის',
        'ლაილაშის', 'ლალიონის', 'ლამის', 'ლამისყანის', 'ლანჩხუთის', 'ლარეხის',
        'ლარსის', 'ლაღიძე მიტროფანეს', 'ლაღიძე რევაზის', 'ლებარდეს',
        'ლეკიშვილის', 'ლენტეხის', 'ლეონიძე გიორგის', 'ლეჟავას', 'ლერმონტოვის',
        'ლერწმის', 'ლესელიძის', 'ლესია უკრაინკას', 'ლეჩხუმის', 'ლიახვის',
        'ლიბანის', 'ლიკანის', 'ლისაშვილის', 'ლიუბოვსკის', 'ლიხაურის', 'ლიხის',
        'ლომაურის', 'ლომთათიძის', 'ლომონოსოვის', 'ლორთქიფანიძე გრიგოლის',
        'ლორთქიფანიძის', 'ლოჭინის', 'ლუბლიანას', 'ლუსიანინის', 'მაზნიაშვილის',
        'მათიაშვილის', 'მაიაკოვსკის', 'მამასახლისოვის', 'მამკოდის', 'მამკოდის',
        'მამრაძის', 'მანაგაძე ალეხსანდეს', 'მანავის', 'მანგლისის',
        'მანიჯაშვილი კახას', 'მანჯგალაძე ეროსის', 'მარაბდის',
        'მარგიანი რევაზის', 'მარელისის', 'მარი ნიკოს', 'მარიჯანის', 'მარტვილის',
        'მარტყოფის', 'მარუაშვილი გიორგის', 'მარუხის გმირების',
        'მარჯანიშვილი კოტეს', 'მარჯანიშვილი კოტეს', 'მაღალაშვილის', 'მაღაროს',
        'მაჩაბელი ივანეს', 'მაჩხაანის', 'მაცესტის', 'მაჭრის', 'მახათას',
        'მახინჯაურის', 'მგალობლიშვილის', 'მებაღიშვილის', 'მეგობრობის',
        'მეგრელაძის', 'მეველეს', 'მელაანის', 'მელიქიშვილის', 'მესხეთის',
        'მესხიას', 'მესხიშვილი ალექსის', 'მესხიშვილის', 'მეტეხის', 'მეუნარგიას',
        'მექანიზაციის', 'მეჯვრისხევის', 'მთავარანგელოზის', 'მთაწმინდის',
        'მთისძირის', 'მიმინოშვილი რომანის', 'მინდელაურის', 'მინდელის',
        'მირზა მეფის', 'მირზაანის', 'მიროტაძის', 'მიტინგის', 'მიქატაძის',
        'მიქატაძის', 'მიქელაძე ევგენის', 'მიქელაძის', 'მიშველაძე არჩილის',
        'მიჩურინის', 'მიცკევიჩის', 'მნათობის', 'მოლითის', 'მოლოკოვის',
        'მორეტის', 'მოსაშვილის', 'მოსე ხონელის', 'მოსიძე ვახტანგის',
        'მოსტკოვის', 'მოსულიშვილის', 'მრევლიშვილის', 'მტკვრის', 'მუკუზანის',
        'მუსხელიშვილის', 'მუხაძის', 'მუხაძის', 'მუხრანის', 'მშველიძის',
        'მცხეთის', 'ნაბახტაურის', 'ნაგომარის', 'ნადიკვარის', 'ნადირაძე კოლაუს',
        'ნავთლუღის', 'ნათაძის', 'ნაკადულის', 'ნიშნიანიძის',
        'ნანეიშვილი ვიქტორის', 'ნანეიშვილი ვლადიმერის', 'ნარგიზის',
        'ნასაკირალის', 'ნასიძე სულხანის', 'ნაქალაქევის', 'ნაქერალას', 'ნიაბის',
        'ნიაღვრის', 'ნიზამის', 'ნიკოლაძე ნიკოს', 'ნინიძის', 'ნიორაძის',
        'ნოვოროსისკის', 'ნონეშვილი იოსების', 'ნოსირის', 'ნოსტეს', 'ნუცუბიძის',
        'ობსერვატორიის', 'ოდესის', 'ონიაშვილის', 'ონის', 'ოჟიოს', 'ორბეთის',
        'ორბელების', 'ორთაჭალის', 'ორპირის', 'ორხევის', 'ოსეთის', 'ოსიაურის',
        'ოფრეთის', 'ოქრომჭედლების', 'ოქროყანის', 'ოჩამჩირის', 'ოცხელების',
        'ოძელაშვილის', 'ოძისის', 'პაიჭაძის', 'პალიასტომის', 'პანკისის',
        'პასტერის', 'პატარიძის', 'პატარძეულის', 'პეტეფი შანდორის',
        'პეტრე იბერის', 'პეტრიაშვილის', 'პეტრიწის', 'პიატიგორსკის', 'პიონერის',
        'პისარევის', 'პლატონის', 'პუშკინი ალექსანდრეს', 'ჟველაურის', 'ჟინვალის',
        'ჟონეთის', 'ჟორესის', 'ჟღენტის', 'რადიანი შალვას', 'რაზიკაშვილის',
        'რაზმაძის', 'რატევანის', 'რატილის', 'რაჭის', 'რევოლუცის', 'რთველაძის',
        'რიონის', 'რიონჰესის', 'რიწის', 'რკინიგზის', 'რკინის', 'როდენის',
        'როსტოვის', 'როსტომაშვილის', 'რუისპირის', 'რუსთაველის', 'რჩეულიშვილის',
        'საადის', 'სააკაძე პაატას', 'სააკაძის', 'საბადურის', 'საბანისძის',
        'საბაშვილის', 'საგარეჯოს', 'საგურამოს', 'სადმელის', 'სავანელის',
        'სათემოს', 'საიათნოვას', 'საირმის', 'სალამის', 'სალხინოს',
        'სამამულო ომის გმირების', 'სამგორის', 'სამტრედიის', 'სამურზაყანოს',
        'სამურის', 'სამღებროს', 'სამღერეთის', 'სამშვილდეს', 'სანავარდოს',
        'სანკტ-პეტერბურგის', 'სარაჯიშვილი დავითის', 'სარაჯიშვილი პეტრეს',
        'სართანიას', 'სართიჭალის', 'სარკინეთის', 'საქანელას', 'საქარის',
        'საყვირის', 'საჩხერის', 'საცხენისის', 'საჭილაოს', 'სახოკიას', 'სევანის',
        'სენაკის', 'სვანეთის', 'გუდაურის', 'სვირის', 'სიონის', 'სიღნაღის',
        'სიხარულიძის', 'სკოლის', 'სომხეთის', 'სოხუმის', 'სოღანლუღის',
        'სპანდარიანის', 'სპარტაკის', 'სტამბის', 'სტანისლავსკის', 'სტურუას',
        'სუვოროვის', 'სულიაშვილის', 'სულხანიშვილის', 'სულხან-საბას',
        'სუმბატაშვილ-იუჟინსკის', 'სუნდუკიანის', 'სურამის', 'სურგულაძის',
        'სხვიტორის', 'სხირტლაძის', 'სხულუხიას', 'ტაბახმელას', 'ტაბიძე ტიციანის',
        'ტანძიის', 'ტარიელის', 'ტატიშვილი ერეკლეს', 'ტატიშვილის', 'ტაშირის',
        'ტაშკენტის', 'ტელეგრაფის', 'ტეტელაშვილის', 'ტეხურის', 'ტვიშის',
        'ტიბაანის', 'ტირიფონის', 'ტიულენევის', 'ტიხონოვის', 'ტოლენჯის',
        'ტოლსტოის', 'ტოლსტონოგოვის', 'ტრანსპორტის', 'ტრაქტორის', 'ტრიკოტაჟის',
        'ტურგენევის', 'ტუსკიას', 'ტყავის', 'ტყეკულტურის', 'ტყვარჩელის',
        'ტყვიავის', 'ტყიბულის', 'ტყის', 'უბილავას', 'უზნაძე დიმიტრის',
        'უზნაძის', 'უიარაღოს', 'უკლება კირილეს', 'უმიკაშვილის', 'უნივერსიტეტის',
        'ურბნისის', 'ურეკის', 'ურიდიას', 'ურიცკის', 'უფლისციხის', 'უშაკოვის',
        'უჩანეიშვილი ირაკლის', 'უწერის', 'უჯარმის', 'ფაბრიკის', 'ფალიაშვილის',
        'ფანასკერტელ-ციციშვილის', 'ფანჯიკიძის', 'ფარავნის', 'ფასანაურის',
        'ფაღავა ირაკლის', 'ფერისცვალების', 'ფიზკულტურის', 'ფილიას', 'ფირდოუსის',
        'ფიროსმანის', 'ფიფიას', 'ფოთის', 'ფოსტის', 'ფოცხვერაშვილის',
        'ფოცხიაშვილი მორისის', 'ფურცელაძის', 'ფშავის', 'ქავთარაძის', 'ქარელის',
        'ქართველიშვილი ლევანის', 'ქართლის', 'ქებურიას', 'ქედის', 'ქერჩის',
        'ქვალონის', 'ქვიშხეთის', 'ქიაჩელის', 'ქიზიყის', 'ქინქლაძე ოთარის',
        'ქინძმარაულის', 'ქიქოძე გერონტის', 'ქობულაძის', 'ქობულეთის', 'ქსნის',
        'ქსოვრელის', 'ქუთათელაძის', 'ქუთათელაძე აპოლონის', 'ქუთაისის',
        'ქუმსიაშვილის', 'ქურდიანი არჩილის', 'ქურდიანი ზაქარიას', 'ქურხულის',
        'ქუჩიშვილის', 'ღამბაშიძის', 'ღრმაღელეს', 'ღუდუშაური ოთარის',
        'ყავლაშვილი შოთას', 'ყარყარაშვილის', 'ყვარელის', 'ყირიმის', 'ყიფიანის',
        'ყიფშიძის', 'ყუშიტაშვილის', 'შავგულიძის', 'შავთელის', 'შავი ზღვის',
        'შავიშვილის', 'შავნაბადას', 'შავსოფელის', 'შანიძე აკაკის',
        'შანშიაშვილის', 'შარაშიძის', 'შარდენის', 'შარტავა ჟიულის',
        'შატბერაშვილის', 'შატილის', 'შაქრიანის', 'შევჩენკო ტარასის',
        'შენგელაიას', 'შერვაშიძის', 'შილდის', 'შინდისის', 'შიო მღვიმელის',
        'შირაქის', 'შოვის', 'შორაპნის', 'შროშის', 'შუამთის', 'შურდულის',
        'შხეფის', 'ჩაიკოვსკის', 'ჩაილურის', 'ჩაისუბნის', 'ჩანჩიბაძის',
        'ჩარგლის', 'ჩარხის', 'ჩაქვის', 'ჩაჩავას', 'ჩახრუხაძის', 'ჩერნიშევსკის',
        'ჩერქეზიშვილის', 'ჩეჩელაშვილის', 'ჩეხოვის', 'ჩიკვანიას', 'ჩიტაიას',
        'ჩიტაძის', 'ჩიქობავა არნოლდის', 'ჩიქოვანის', 'ჩკალოვის',
        'ჩოლოყაშვილი ქაიხოსროს', 'ჩოჩუას', 'ჩოხატაურის', 'ჩოხელის',
        'ჩუბინაშვილი გიორგის', 'ჩუბინიძის', 'ჩხიკვაძის', 'ცაბაძე გიორგის',
        'ცაგარელი არჩილის', 'ცაგერის', 'ცაიშის', 'ცემის', 'ციმაკურიძის',
        'ცინცაძე კალისტრატეს', 'ცისარტკელას', 'ცისკრის', 'ციხისძირის',
        'ცოდნისკარის', 'ცურტაველი იაკობის', 'ცუცქირიძის', 'ცხემის', 'ცხვედაძის',
        'ცხრა აპრილის', 'ცხრა ძმის', 'ძეგამის', 'ძევერის', 'ძმობის',
        'ძოწენიძის', 'წავკისის', 'წალენჯიხის', 'წალკის', 'წაღვერის', 'წერეთლის',
        'წერნაკის', 'წერონისის', 'წიკლაურის', 'წინამძღვრიშვილის',
        'წინამძღვრიშვილის', 'წინანაურის', 'წინანდლის', 'წინაუბნის',
        'წიწამურის', 'წმ. ნიკოლოზის', 'წნორისწყლის', 'წრომის', 'წულაძის',
        'წულუკიძის', 'წურწუმიას', 'წუწუნავას', 'წუწხვატის', 'წყალსადენის',
        'წყალტუბოს', 'წყაროს', 'ჭაბუკიანი ვახტანგის', 'ჭავჭავაძე ზურაბის',
        'ჭავჭავაძე ალექსანდრეს', 'ჭალადიდის', 'ჭანტურია გიას', 'ჭიათურის',
        'ჭიაურელი მიხეილის', 'ჭიჭინაძე ზაქარიას', 'ჭოველიძე თამარის',
        'ჭონქაძე დანიელის', 'ჭოპორტის', 'ჭოროხის', 'ჭრებალოს', 'ჭრელაშვილის',
        'ხაბეიშვილის', 'ხაზინის', 'ხანძთელი გრიგოლის', 'ხარაბაძის',
        'ხარაგაულის', 'ხარფუხის', 'ხაჩატურიანის', 'ხევის', 'ხევისუბნის',
        'ხევსურეთის', 'ხევძმარის', 'ხეთაგუროვის', 'ხერგიანის', 'ხერთვისის',
        'ხერხეულიძეების', 'ხეჩუაშვილის', 'ხვამლის', 'ხვანჭკარის', 'ხვედელიანის',
        'ხვინგიას', 'ხვიჩია იპოლიტეს', 'ხიდის', 'ხიდისთავის', 'ხივინის',
        'ხიმშიაშვილის', 'ხმელნიცკის', 'ხოდაშენის', 'ხომლელის', 'ხონის',
        'ხორავა აკაკის', 'ხორნაბუჯის', 'ხოშარაულის', 'ხრამჰესის', 'ხრესილის',
        'ხუდადოვის', 'ჯაბაურის', 'ჯაბიძის', 'ჯავახეთის', 'ჯავახიშვილი ივანეს',
        'ჯავახიშვილი მიხეილის', 'ჯავის', 'ჯამბულის', 'ჯანაშვილის', 'ჯანაშიას',
        'ჯანჯღავას', 'ჯვარედინის', 'პოლიტკოვსკაიას', 'ჯიქიას', 'ჯორბენაძის',
        'ჯორჯაძის', 'ჰოსპიტალის',
    )

    # Source: List of cities and towns in Georgia (Wikipedia)
    # https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Georgia_(country)
    city_names = (
        'აბაშა', 'ამბროლაური', 'ახალი ათონი', 'ახალქალაქი', 'ახალციხე',
        'ახმეტა', 'ბათუმი', 'ბაღდათი', 'ბოლნისი', 'ბორჯომი', 'გაგრა', 'გალი',
        'გარდაბანი', 'გორი', 'გუდაუთა', 'გურჯაანი', 'დედოფლისწყარო', 'დმანისი',
        'დუშეთი', 'ვალე', 'ვანი', 'ზესტაფონი', 'ზუგდიდი', 'თბილისი',
        'თეთრიწყარო', 'თელავი', 'თერჯოლა', 'კასპი', 'ლაგოდეხი', 'ლანჩხუთი',
        'მარნეული', 'მარტვილი', 'მცხეთა', 'ნინოწმინდა', 'ოზურგეთი', 'ონი',
        'ოჩამჩირე', 'რუსთავი', 'საგარეჯო', 'სამტრედია', 'საჩხერე', 'სენაკი',
        'სიღნაღი', 'სოხუმი', 'ტყვარჩელი', 'ტყიბული', 'ფოთი', 'ქარელი',
        'ქობულეთი', 'ქუთაისი', 'ყვარელი', 'ცაგერი', 'ცხინვალი', 'წალენჯიხა',
        'წალკა', 'წნორი', 'წყალტუბო', 'ჭიათურა', 'ხაშური', 'ხობი', 'ხონი',
        'ჯვარი',
    )

    def street_title(self):
        return self.random_element(self.street_titles)

    def city_name(self):
        return self.random_element(self.city_names)
