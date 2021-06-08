#!pip install --upgrade pandas
#!pip install --upgrade requests
#!pip install --upgrade bs4
#!pip install --upgrade joblib

#!pip install python-whois
#!pip install favicon
#!pip install tldextract

#dates manipulation
import datetime

#To count vowels and signs
from collections import Counter

#Regular Expressions
import re

# Text of webpage
from bs4 import BeautifulSoup


#Connect to url
import requests

#To check favicon of url
import favicon

#Data from whois domain database
import whois

#url parsing
import tldextract
from urllib.parse import urlparse


#check ssl certificate
import socket
import ssl

#https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#https://stackoverflow.com/a/28002687/11444424

# Active urls
from is_active import check_active_url


vowels = 'aeiou'
list_of_signs = '.-_/@&'
dict_of_signs = {
                    '.' : 'dot',
                    '-' : 'hyphen',
                    '_' : 'underline',
                    '/' : 'slash',
                    '@' : 'at',
                    '&' : 'and'
    }
set_of_worst_tlds = set(['surf' , 'fail' , 'gq', 'viajes' , 'ml' , 'cf', 'london', 'exposed', 'ga' ,'tk'] )
list_of_TLDs = set(['AAA', 'AARP', 'ABARTH', 'ABB', 'ABBOTT', 'ABBVIE', 'ABC', 'ABLE', 'ABOGADO', 'ABUDHABI', 'AC', 'ACADEMY', 'ACCENTURE', 'ACCOUNTANT', 'ACCOUNTANTS', 'ACO', 'ACTOR', 'AD', 'ADAC', 'ADS', 'ADULT', 'AE', 'AEG', 'AERO', 'AETNA', 'AF', 'AFAMILYCOMPANY', 'AFL', 'AFRICA', 'AG', 'AGAKHAN', 'AGENCY', 'AI', 'AIG', 'AIRBUS', 'AIRFORCE', 'AIRTEL', 'AKDN', 'AL', 'ALFAROMEO', 'ALIBABA', 'ALIPAY', 'ALLFINANZ', 'ALLSTATE', 'ALLY', 'ALSACE', 'ALSTOM', 'AM', 'AMAZON', 'AMERICANEXPRESS', 'AMERICANFAMILY', 'AMEX', 'AMFAM', 'AMICA', 'AMSTERDAM', 'ANALYTICS', 'ANDROID', 'ANQUAN', 'ANZ', 'AO', 'AOL', 'APARTMENTS', 'APP', 'APPLE', 'AQ', 'AQUARELLE', 'AR', 'ARAB', 'ARAMCO', 'ARCHI', 'ARMY', 'ARPA', 'ART', 'ARTE', 'AS', 'ASDA', 'ASIA', 'ASSOCIATES', 'AT', 'ATHLETA', 'ATTORNEY', 'AU', 'AUCTION', 'AUDI', 'AUDIBLE', 'AUDIO', 'AUSPOST', 'AUTHOR', 'AUTO', 'AUTOS', 'AVIANCA', 'AW', 'AWS', 'AX', 'AXA', 'AZ', 'AZURE', 'BA', 'BABY', 'BAIDU', 'BANAMEX', 'BANANAREPUBLIC', 'BAND', 'BANK', 'BAR', 'BARCELONA', 'BARCLAYCARD', 'BARCLAYS', 'BAREFOOT', 'BARGAINS', 'BASEBALL', 'BASKETBALL', 'BAUHAUS', 'BAYERN', 'BB', 'BBC', 'BBT', 'BBVA', 'BCG', 'BCN', 'BD', 'BE', 'BEATS', 'BEAUTY', 'BEER', 'BENTLEY', 'BERLIN', 'BEST', 'BESTBUY', 'BET', 'BF', 'BG', 'BH', 'BHARTI', 'BI', 'BIBLE', 'BID', 'BIKE', 'BING', 'BINGO', 'BIO', 'BIZ', 'BJ', 'BLACK', 'BLACKFRIDAY', 'BLOCKBUSTER', 'BLOG', 'BLOOMBERG', 'BLUE', 'BM', 'BMS', 'BMW', 'BN', 'BNPPARIBAS', 'BO', 'BOATS', 'BOEHRINGER', 'BOFA', 'BOM', 'BOND', 'BOO', 'BOOK', 'BOOKING', 'BOSCH', 'BOSTIK', 'BOSTON', 'BOT', 'BOUTIQUE', 'BOX', 'BR', 'BRADESCO', 'BRIDGESTONE', 'BROADWAY', 'BROKER', 'BROTHER', 'BRUSSELS', 'BS', 'BT', 'BUDAPEST', 'BUGATTI', 'BUILD', 'BUILDERS', 'BUSINESS', 'BUY', 'BUZZ', 'BV', 'BW', 'BY', 'BZ', 'BZH', 'CA', 'CAB', 'CAFE', 'CAL', 'CALL', 'CALVINKLEIN', 'CAM', 'CAMERA', 'CAMP', 'CANCERRESEARCH', 'CANON', 'CAPETOWN', 'CAPITAL', 'CAPITALONE', 'CAR', 'CARAVAN', 'CARDS', 'CARE', 'CAREER', 'CAREERS', 'CARS', 'CASA', 'CASE', 'CASH', 'CASINO', 'CAT', 'CATERING', 'CATHOLIC', 'CBA', 'CBN', 'CBRE', 'CBS', 'CC', 'CD', 'CENTER', 'CEO', 'CERN', 'CF', 'CFA', 'CFD', 'CG', 'CH', 'CHANEL', 'CHANNEL', 'CHARITY', 'CHASE', 'CHAT', 'CHEAP', 'CHINTAI', 'CHRISTMAS', 'CHROME', 'CHURCH', 'CI', 'CIPRIANI', 'CIRCLE', 'CISCO', 'CITADEL', 'CITI', 'CITIC', 'CITY', 'CITYEATS', 'CK', 'CL', 'CLAIMS', 'CLEANING', 'CLICK', 'CLINIC', 'CLINIQUE', 'CLOTHING', 'CLOUD', 'CLUB', 'CLUBMED', 'CM', 'CN', 'CO', 'COACH', 'CODES', 'COFFEE', 'COLLEGE', 'COLOGNE', 'COM', 'COMCAST', 'COMMBANK', 'COMMUNITY', 'COMPANY', 'COMPARE', 'COMPUTER', 'COMSEC', 'CONDOS', 'CONSTRUCTION', 'CONSULTING', 'CONTACT', 'CONTRACTORS', 'COOKING', 'COOKINGCHANNEL', 'COOL', 'COOP', 'CORSICA', 'COUNTRY', 'COUPON', 'COUPONS', 'COURSES', 'CPA', 'CR', 'CREDIT', 'CREDITCARD', 'CREDITUNION', 'CRICKET', 'CROWN', 'CRS', 'CRUISE', 'CRUISES', 'CSC', 'CU', 'CUISINELLA', 'CV', 'CW', 'CX', 'CY', 'CYMRU', 'CYOU', 'CZ', 'DABUR', 'DAD', 'DANCE', 'DATA', 'DATE', 'DATING', 'DATSUN', 'DAY', 'DCLK', 'DDS', 'DE', 'DEAL', 'DEALER', 'DEALS', 'DEGREE', 'DELIVERY', 'DELL', 'DELOITTE', 'DELTA', 'DEMOCRAT', 'DENTAL', 'DENTIST', 'DESI', 'DESIGN', 'DEV', 'DHL', 'DIAMONDS', 'DIET', 'DIGITAL', 'DIRECT', 'DIRECTORY', 'DISCOUNT', 'DISCOVER', 'DISH', 'DIY', 'DJ', 'DK', 'DM', 'DNP', 'DO', 'DOCS', 'DOCTOR', 'DOG', 'DOMAINS', 'DOT', 'DOWNLOAD', 'DRIVE', 'DTV', 'DUBAI', 'DUCK', 'DUNLOP', 'DUPONT', 'DURBAN', 'DVAG', 'DVR', 'DZ', 'EARTH', 'EAT', 'EC', 'ECO', 'EDEKA', 'EDU', 'EDUCATION', 'EE', 'EG', 'EMAIL', 'EMERCK', 'ENERGY', 'ENGINEER', 'ENGINEERING', 'ENTERPRISES', 'EPSON', 'EQUIPMENT', 'ER', 'ERICSSON', 'ERNI', 'ES', 'ESQ', 'ESTATE', 'ET', 'ETISALAT', 'EU', 'EUROVISION', 'EUS', 'EVENTS', 'EXCHANGE', 'EXPERT', 'EXPOSED', 'EXPRESS', 'EXTRASPACE', 'FAGE', 'FAIL', 'FAIRWINDS', 'FAITH', 'FAMILY', 'FAN', 'FANS', 'FARM', 'FARMERS', 'FASHION', 'FAST', 'FEDEX', 'FEEDBACK', 'FERRARI', 'FERRERO', 'FI', 'FIAT', 'FIDELITY', 'FIDO', 'FILM', 'FINAL', 'FINANCE', 'FINANCIAL', 'FIRE', 'FIRESTONE', 'FIRMDALE', 'FISH', 'FISHING', 'FIT', 'FITNESS', 'FJ', 'FK', 'FLICKR', 'FLIGHTS', 'FLIR', 'FLORIST', 'FLOWERS', 'FLY', 'FM', 'FO', 'FOO', 'FOOD', 'FOODNETWORK', 'FOOTBALL', 'FORD', 'FOREX', 'FORSALE', 'FORUM', 'FOUNDATION', 'FOX', 'FR', 'FREE', 'FRESENIUS', 'FRL', 'FROGANS', 'FRONTDOOR', 'FRONTIER', 'FTR', 'FUJITSU', 'FUJIXEROX', 'FUN', 'FUND', 'FURNITURE', 'FUTBOL', 'FYI', 'GA', 'GAL', 'GALLERY', 'GALLO', 'GALLUP', 'GAME', 'GAMES', 'GAP', 'GARDEN', 'GAY', 'GB', 'GBIZ', 'GD', 'GDN', 'GE', 'GEA', 'GENT', 'GENTING', 'GEORGE', 'GF', 'GG', 'GGEE', 'GH', 'GI', 'GIFT', 'GIFTS', 'GIVES', 'GIVING', 'GL', 'GLADE', 'GLASS', 'GLE', 'GLOBAL', 'GLOBO', 'GM', 'GMAIL', 'GMBH', 'GMO', 'GMX', 'GN', 'GODADDY', 'GOLD', 'GOLDPOINT', 'GOLF', 'GOO', 'GOODYEAR', 'GOOG', 'GOOGLE', 'GOP', 'GOT', 'GOV', 'GP', 'GQ', 'GR', 'GRAINGER', 'GRAPHICS', 'GRATIS', 'GREEN', 'GRIPE', 'GROCERY', 'GROUP', 'GS', 'GT', 'GU', 'GUARDIAN', 'GUCCI', 'GUGE', 'GUIDE', 'GUITARS', 'GURU', 'GW', 'GY', 'HAIR', 'HAMBURG', 'HANGOUT', 'HAUS', 'HBO', 'HDFC', 'HDFCBANK', 'HEALTH', 'HEALTHCARE', 'HELP', 'HELSINKI', 'HERE', 'HERMES', 'HGTV', 'HIPHOP', 'HISAMITSU', 'HITACHI', 'HIV', 'HK', 'HKT', 'HM', 'HN', 'HOCKEY', 'HOLDINGS', 'HOLIDAY', 'HOMEDEPOT', 'HOMEGOODS', 'HOMES', 'HOMESENSE', 'HONDA', 'HORSE', 'HOSPITAL', 'HOST', 'HOSTING', 'HOT', 'HOTELES', 'HOTELS', 'HOTMAIL', 'HOUSE', 'HOW', 'HR', 'HSBC', 'HT', 'HU', 'HUGHES', 'HYATT', 'HYUNDAI', 'IBM', 'ICBC', 'ICE', 'ICU', 'ID', 'IE', 'IEEE', 'IFM', 'IKANO', 'IL', 'IM', 'IMAMAT', 'IMDB', 'IMMO', 'IMMOBILIEN', 'IN', 'INC', 'INDUSTRIES', 'INFINITI', 'INFO', 'ING', 'INK', 'INSTITUTE', 'INSURANCE', 'INSURE', 'INT', 'INTERNATIONAL', 'INTUIT', 'INVESTMENTS', 'IO', 'IPIRANGA', 'IQ', 'IR', 'IRISH', 'IS', 'ISMAILI', 'IST', 'ISTANBUL', 'IT', 'ITAU', 'ITV', 'IVECO', 'JAGUAR', 'JAVA', 'JCB', 'JE', 'JEEP', 'JETZT', 'JEWELRY', 'JIO', 'JLL', 'JM', 'JMP', 'JNJ', 'JO', 'JOBS', 'JOBURG', 'JOT', 'JOY', 'JP', 'JPMORGAN', 'JPRS', 'JUEGOS', 'JUNIPER', 'KAUFEN', 'KDDI', 'KE', 'KERRYHOTELS', 'KERRYLOGISTICS', 'KERRYPROPERTIES', 'KFH', 'KG', 'KH', 'KI', 'KIA', 'KIM', 'KINDER', 'KINDLE', 'KITCHEN', 'KIWI', 'KM', 'KN', 'KOELN', 'KOMATSU', 'KOSHER', 'KP', 'KPMG', 'KPN', 'KR', 'KRD', 'KRED', 'KUOKGROUP', 'KW', 'KY', 'KYOTO', 'KZ', 'LA', 'LACAIXA', 'LAMBORGHINI', 'LAMER', 'LANCASTER', 'LANCIA', 'LAND', 'LANDROVER', 'LANXESS', 'LASALLE', 'LAT', 'LATINO', 'LATROBE', 'LAW', 'LAWYER', 'LB', 'LC', 'LDS', 'LEASE', 'LECLERC', 'LEFRAK', 'LEGAL', 'LEGO', 'LEXUS', 'LGBT', 'LI', 'LIDL', 'LIFE', 'LIFEINSURANCE', 'LIFESTYLE', 'LIGHTING', 'LIKE', 'LILLY', 'LIMITED', 'LIMO', 'LINCOLN', 'LINDE', 'LINK', 'LIPSY', 'LIVE', 'LIVING', 'LIXIL', 'LK', 'LLC', 'LLP', 'LOAN', 'LOANS', 'LOCKER', 'LOCUS', 'LOFT', 'LOL', 'LONDON', 'LOTTE', 'LOTTO', 'LOVE', 'LPL', 'LPLFINANCIAL', 'LR', 'LS', 'LT', 'LTD', 'LTDA', 'LU', 'LUNDBECK', 'LUXE', 'LUXURY', 'LV', 'LY', 'MA', 'MACYS', 'MADRID', 'MAIF', 'MAISON', 'MAKEUP', 'MAN', 'MANAGEMENT', 'MANGO', 'MAP', 'MARKET', 'MARKETING', 'MARKETS', 'MARRIOTT', 'MARSHALLS', 'MASERATI', 'MATTEL', 'MBA', 'MC', 'MCKINSEY', 'MD', 'ME', 'MED', 'MEDIA', 'MEET', 'MELBOURNE', 'MEME', 'MEMORIAL', 'MEN', 'MENU', 'MERCKMSD', 'MG', 'MH', 'MIAMI', 'MICROSOFT', 'MIL', 'MINI', 'MINT', 'MIT', 'MITSUBISHI', 'MK', 'ML', 'MLB', 'MLS', 'MM', 'MMA', 'MN', 'MO', 'MOBI', 'MOBILE', 'MODA', 'MOE', 'MOI', 'MOM', 'MONASH', 'MONEY', 'MONSTER', 'MORMON', 'MORTGAGE', 'MOSCOW', 'MOTO', 'MOTORCYCLES', 'MOV', 'MOVIE', 'MP', 'MQ', 'MR', 'MS', 'MSD', 'MT', 'MTN', 'MTR', 'MU', 'MUSEUM', 'MUTUAL', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NAB', 'NAGOYA', 'NAME', 'NATIONWIDE', 'NATURA', 'NAVY', 'NBA', 'NC', 'NE', 'NEC', 'NET', 'NETBANK', 'NETFLIX', 'NETWORK', 'NEUSTAR', 'NEW', 'NEWS', 'NEXT', 'NEXTDIRECT', 'NEXUS', 'NF', 'NFL', 'NG', 'NGO', 'NHK', 'NI', 'NICO', 'NIKE', 'NIKON', 'NINJA', 'NISSAN', 'NISSAY', 'NL', 'NO', 'NOKIA', 'NORTHWESTERNMUTUAL', 'NORTON', 'NOW', 'NOWRUZ', 'NOWTV', 'NP', 'NR', 'NRA', 'NRW', 'NTT', 'NU', 'NYC', 'NZ', 'OBI', 'OBSERVER', 'OFF', 'OFFICE', 'OKINAWA', 'OLAYAN', 'OLAYANGROUP', 'OLDNAVY', 'OLLO', 'OM', 'OMEGA', 'ONE', 'ONG', 'ONL', 'ONLINE', 'ONYOURSIDE', 'OOO', 'OPEN', 'ORACLE', 'ORANGE', 'ORG', 'ORGANIC', 'ORIGINS', 'OSAKA', 'OTSUKA', 'OTT', 'OVH', 'PA', 'PAGE', 'PANASONIC', 'PARIS', 'PARS', 'PARTNERS', 'PARTS', 'PARTY', 'PASSAGENS', 'PAY', 'PCCW', 'PE', 'PET', 'PF', 'PFIZER', 'PG', 'PH', 'PHARMACY', 'PHD', 'PHILIPS', 'PHONE', 'PHOTO', 'PHOTOGRAPHY', 'PHOTOS', 'PHYSIO', 'PICS', 'PICTET', 'PICTURES', 'PID', 'PIN', 'PING', 'PINK', 'PIONEER', 'PIZZA', 'PK', 'PL', 'PLACE', 'PLAY', 'PLAYSTATION', 'PLUMBING', 'PLUS', 'PM', 'PN', 'PNC', 'POHL', 'POKER', 'POLITIE', 'PORN', 'POST', 'PR', 'PRAMERICA', 'PRAXI', 'PRESS', 'PRIME', 'PRO', 'PROD', 'PRODUCTIONS', 'PROF', 'PROGRESSIVE', 'PROMO', 'PROPERTIES', 'PROPERTY', 'PROTECTION', 'PRU', 'PRUDENTIAL', 'PS', 'PT', 'PUB', 'PW', 'PWC', 'PY', 'QA', 'QPON', 'QUEBEC', 'QUEST', 'QVC', 'RACING', 'RADIO', 'RAID', 'RE', 'READ', 'REALESTATE', 'REALTOR', 'REALTY', 'RECIPES', 'RED', 'REDSTONE', 'REDUMBRELLA', 'REHAB', 'REISE', 'REISEN', 'REIT', 'RELIANCE', 'REN', 'RENT', 'RENTALS', 'REPAIR', 'REPORT', 'REPUBLICAN', 'REST', 'RESTAURANT', 'REVIEW', 'REVIEWS', 'REXROTH', 'RICH', 'RICHARDLI', 'RICOH', 'RIL', 'RIO', 'RIP', 'RMIT', 'RO', 'ROCHER', 'ROCKS', 'RODEO', 'ROGERS', 'ROOM', 'RS', 'RSVP', 'RU', 'RUGBY', 'RUHR', 'RUN', 'RW', 'RWE', 'RYUKYU', 'SA', 'SAARLAND', 'SAFE', 'SAFETY', 'SAKURA', 'SALE', 'SALON', 'SAMSCLUB', 'SAMSUNG', 'SANDVIK', 'SANDVIKCOROMANT', 'SANOFI', 'SAP', 'SARL', 'SAS', 'SAVE', 'SAXO', 'SB', 'SBI', 'SBS', 'SC', 'SCA', 'SCB', 'SCHAEFFLER', 'SCHMIDT', 'SCHOLARSHIPS', 'SCHOOL', 'SCHULE', 'SCHWARZ', 'SCIENCE', 'SCJOHNSON', 'SCOT', 'SD', 'SE', 'SEARCH', 'SEAT', 'SECURE', 'SECURITY', 'SEEK', 'SELECT', 'SENER', 'SERVICES', 'SES', 'SEVEN', 'SEW', 'SEX', 'SEXY', 'SFR', 'SG', 'SH', 'SHANGRILA', 'SHARP', 'SHAW', 'SHELL', 'SHIA', 'SHIKSHA', 'SHOES', 'SHOP', 'SHOPPING', 'SHOUJI', 'SHOW', 'SHOWTIME', 'SI', 'SILK', 'SINA', 'SINGLES', 'SITE', 'SJ', 'SK', 'SKI', 'SKIN', 'SKY', 'SKYPE', 'SL', 'SLING', 'SM', 'SMART', 'SMILE', 'SN', 'SNCF', 'SO', 'SOCCER', 'SOCIAL', 'SOFTBANK', 'SOFTWARE', 'SOHU', 'SOLAR', 'SOLUTIONS', 'SONG', 'SONY', 'SOY', 'SPA', 'SPACE', 'SPORT', 'SPOT', 'SPREADBETTING', 'SR', 'SRL', 'SS', 'ST', 'STADA', 'STAPLES', 'STAR', 'STATEBANK', 'STATEFARM', 'STC', 'STCGROUP', 'STOCKHOLM', 'STORAGE', 'STORE', 'STREAM', 'STUDIO', 'STUDY', 'STYLE', 'SU', 'SUCKS', 'SUPPLIES', 'SUPPLY', 'SUPPORT', 'SURF', 'SURGERY', 'SUZUKI', 'SV', 'SWATCH', 'SWIFTCOVER', 'SWISS', 'SX', 'SY', 'SYDNEY', 'SYSTEMS', 'SZ', 'TAB', 'TAIPEI', 'TALK', 'TAOBAO', 'TARGET', 'TATAMOTORS', 'TATAR', 'TATTOO', 'TAX', 'TAXI', 'TC', 'TCI', 'TD', 'TDK', 'TEAM', 'TECH', 'TECHNOLOGY', 'TEL', 'TEMASEK', 'TENNIS', 'TEVA', 'TF', 'TG', 'TH', 'THD', 'THEATER', 'THEATRE', 'TIAA', 'TICKETS', 'TIENDA', 'TIFFANY', 'TIPS', 'TIRES', 'TIROL', 'TJ', 'TJMAXX', 'TJX', 'TK', 'TKMAXX', 'TL', 'TM', 'TMALL', 'TN', 'TO', 'TODAY', 'TOKYO', 'TOOLS', 'TOP', 'TORAY', 'TOSHIBA', 'TOTAL', 'TOURS', 'TOWN', 'TOYOTA', 'TOYS', 'TR', 'TRADE', 'TRADING', 'TRAINING', 'TRAVEL', 'TRAVELCHANNEL', 'TRAVELERS', 'TRAVELERSINSURANCE', 'TRUST', 'TRV', 'TT', 'TUBE', 'TUI', 'TUNES', 'TUSHU', 'TV', 'TVS', 'TW', 'TZ', 'UA', 'UBANK', 'UBS', 'UG', 'UK', 'UNICOM', 'UNIVERSITY', 'UNO', 'UOL', 'UPS', 'US', 'UY', 'UZ', 'VA', 'VACATIONS', 'VANA', 'VANGUARD', 'VC', 'VE', 'VEGAS', 'VENTURES', 'VERISIGN', 'VERSICHERUNG', 'VET', 'VG', 'VI', 'VIAJES', 'VIDEO', 'VIG', 'VIKING', 'VILLAS', 'VIN', 'VIP', 'VIRGIN', 'VISA', 'VISION', 'VIVA', 'VIVO', 'VLAANDEREN', 'VN', 'VODKA', 'VOLKSWAGEN', 'VOLVO', 'VOTE', 'VOTING', 'VOTO', 'VOYAGE', 'VU', 'VUELOS', 'WALES', 'WALMART', 'WALTER', 'WANG', 'WANGGOU', 'WATCH', 'WATCHES', 'WEATHER', 'WEATHERCHANNEL', 'WEBCAM', 'WEBER', 'WEBSITE', 'WED', 'WEDDING', 'WEIBO', 'WEIR', 'WF', 'WHOSWHO', 'WIEN', 'WIKI', 'WILLIAMHILL', 'WIN', 'WINDOWS', 'WINE', 'WINNERS', 'WME', 'WOLTERSKLUWER', 'WOODSIDE', 'WORK', 'WORKS', 'WORLD', 'WOW', 'WS', 'WTC', 'WTF', 'XBOX', 'XEROX', 'XFINITY', 'XIHUAN', 'XIN', 'XN--11B4C3D', 'XN--1CK2E1B', 'XN--1QQW23A', 'XN--2SCRJ9C', 'XN--30RR7Y', 'XN--3BST00M', 'XN--3DS443G', 'XN--3E0B707E', 'XN--3HCRJ9C', 'XN--3OQ18VL8PN36A', 'XN--3PXU8K', 'XN--42C2D9A', 'XN--45BR5CYL', 'XN--45BRJ9C', 'XN--45Q11C', 'XN--4DBRK0CE', 'XN--4GBRIM', 'XN--54B7FTA0CC', 'XN--55QW42G', 'XN--55QX5D', 'XN--5SU34J936BGSG', 'XN--5TZM5G', 'XN--6FRZ82G', 'XN--6QQ986B3XL', 'XN--80ADXHKS', 'XN--80AO21A', 'XN--80AQECDR1A', 'XN--80ASEHDB', 'XN--80ASWG', 'XN--8Y0A063A', 'XN--90A3AC', 'XN--90AE', 'XN--90AIS', 'XN--9DBQ2A', 'XN--9ET52U', 'XN--9KRT00A', 'XN--B4W605FERD', 'XN--BCK1B9A5DRE4C', 'XN--C1AVG', 'XN--C2BR7G', 'XN--CCK2B3B', 'XN--CCKWCXETD', 'XN--CG4BKI', 'XN--CLCHC0EA0B2G2A9GCD', 'XN--CZR694B', 'XN--CZRS0T', 'XN--CZRU2D', 'XN--D1ACJ3B', 'XN--D1ALF', 'XN--E1A4C', 'XN--ECKVDTC9D', 'XN--EFVY88H', 'XN--FCT429K', 'XN--FHBEI', 'XN--FIQ228C5HS', 'XN--FIQ64B', 'XN--FIQS8S', 'XN--FIQZ9S', 'XN--FJQ720A', 'XN--FLW351E', 'XN--FPCRJ9C3D', 'XN--FZC2C9E2C', 'XN--FZYS8D69UVGM', 'XN--G2XX48C', 'XN--GCKR3F0F', 'XN--GECRJ9C', 'XN--GK3AT1E', 'XN--H2BREG3EVE', 'XN--H2BRJ9C', 'XN--H2BRJ9C8C', 'XN--HXT814E', 'XN--I1B6B1A6A2E', 'XN--IMR513N', 'XN--IO0A7I', 'XN--J1AEF', 'XN--J1AMH', 'XN--J6W193G', 'XN--JLQ480N2RG', 'XN--JLQ61U9W7B', 'XN--JVR189M', 'XN--KCRX77D1X4A', 'XN--KPRW13D', 'XN--KPRY57D', 'XN--KPUT3I', 'XN--L1ACC', 'XN--LGBBAT1AD8J', 'XN--MGB9AWBF', 'XN--MGBA3A3EJT', 'XN--MGBA3A4F16A', 'XN--MGBA7C0BBN0A', 'XN--MGBAAKC7DVF', 'XN--MGBAAM7A8H', 'XN--MGBAB2BD', 'XN--MGBAH1A3HJKRD', 'XN--MGBAI9AZGQP6J', 'XN--MGBAYH7GPA', 'XN--MGBBH1A', 'XN--MGBBH1A71E', 'XN--MGBC0A9AZCG', 'XN--MGBCA7DZDO', 'XN--MGBCPQ6GPA1A', 'XN--MGBERP4A5D4AR', 'XN--MGBGU82A', 'XN--MGBI4ECEXP', 'XN--MGBPL2FH', 'XN--MGBT3DHD', 'XN--MGBTX2B', 'XN--MGBX4CD0AB', 'XN--MIX891F', 'XN--MK1BU44C', 'XN--MXTQ1M', 'XN--NGBC5AZD', 'XN--NGBE9E0A', 'XN--NGBRX', 'XN--NODE', 'XN--NQV7F', 'XN--NQV7FS00EMA', 'XN--NYQY26A', 'XN--O3CW4H', 'XN--OGBPF8FL', 'XN--OTU796D', 'XN--P1ACF', 'XN--P1AI', 'XN--PGBS0DH', 'XN--PSSY2U', 'XN--Q7CE6A', 'XN--Q9JYB4C', 'XN--QCKA1PMC', 'XN--QXA6A', 'XN--QXAM', 'XN--RHQV96G', 'XN--ROVU88B', 'XN--RVC1E0AM3E', 'XN--S9BRJ9C', 'XN--SES554G', 'XN--T60B56A', 'XN--TCKWE', 'XN--TIQ49XQYJ', 'XN--UNUP4Y', 'XN--VERMGENSBERATER-CTB', 'XN--VERMGENSBERATUNG-PWB', 'XN--VHQUV', 'XN--VUQ861B', 'XN--W4R85EL8FHU5DNRA', 'XN--W4RS40L', 'XN--WGBH1C', 'XN--WGBL6A', 'XN--XHQ521B', 'XN--XKC2AL3HYE2A', 'XN--XKC2DL3A5EE0H', 'XN--Y9A3AQ', 'XN--YFRO4I67O', 'XN--YGBI2AMMX', 'XN--ZFR164B', 'XXX', 'XYZ', 'YACHTS', 'YAHOO', 'YAMAXUN', 'YANDEX', 'YE', 'YODOBASHI', 'YOGA', 'YOKOHAMA', 'YOU', 'YOUTUBE', 'YT', 'YUN', 'ZA', 'ZAPPOS', 'ZARA', 'ZERO', 'ZIP', 'ZM', 'ZONE', 'ZUERICH', 'ZW'])

#'qty_' + dict_of_signs[sign] + '_' + name
def count_signs ( url , sign):
  count = Counter(url)
  return count[sign] if sign in url else 0

#qty_vowels_domain
def count_vowels ( domain ):
  count = Counter(domain)
  cnt = 0
  for vowel in vowels :
    if vowel in domain :
      cnt += count[vowel]
  return cnt

#has_double_slash_
def double_slash (url) :
  if not url.startswith('http'):
    length = 1
  else :
    length = 2
  splited_url = url.split('//')
  return 1 if len(splited_url) > length else 0

#name+'_length'
def count_length(url):
  return len(url)

#server_client_domain
def client_server(domain):
  return 1 if 'client' in domain or 'server' in domain else 0

#domain_in_ip
def domain_ip(domain):
  return 1 if len(re.findall( r'[0-9]+(?:\.[0-9]+){3}', domain ) ) > 0  else  0
            
#https://stackoverflow.com/a/42408099/11444424
def email_in_url(url):
  return 1 if len(re.findall(r'[\w\.-]+@[\w\.-]+', url)) > 0  else 0


def scriptInUrl(url):
  if 'script' in url :
    return 1
  return 0

def tld_in_params(params):
  for TLD in set_of_worst_tlds:
      if '.'+TLD.lower() in params :
          return 2 
  for TLD in list_of_TLDs:
      if '.'+TLD.lower() in params :
          return 1 
  return 0 

#PARAMETERS
def count_params (params):
  if params != '' :
    return params.count('&') + 1
  else :
    return 0

#https://github.com/himanshi18037/WhatAPhish/blob/main/Features_For_New_DataPoint.ipynb 
def favicon_anchor_whois_days(url):
  extract_res = tldextract.extract(url)
  url_ref = extract_res.domain 
  try :
    favs = favicon.get(url,timeout=2)
    match = 0
    for favi in favs:
      url2 = favi.url
      extract_res2 = tldextract.extract(url2)
      url_ref2 = extract_res2.domain

      if url_ref in url_ref2:
        match += 1

    if match >= len(favs)/2:
      favicon_return = 0
    else :
      favicon_return = 1
  except :
    favicon_return = 0
  
  try :
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    a_tags = soup.find_all('a')
    if len(a_tags) == 0:
      anchor_return = 0
    else :
      invalid = ['#', '#content', '#skip', 'JavaScript::void(0)']
      bad_count = 0
      for t in a_tags:
        link = t['href']

        if link in invalid:
          bad_count += 1

        if url_validator(link):
          extract_res2 = tldextract.extract(link)
          url_ref2 = extract_res2.domain

          if url_ref not in url_ref2:
            bad_count += 1

      bad_count /= len(a_tags)
    
      anchor_return =  bad_count
  except :
    anchor_return =  -1
  
  domain = extract_res.domain + "." + extract_res.suffix
  try:
    whois_res = whois.whois(domain)
    whois_return = 0 
    whois_days =(datetime.datetime.now() - whois_res["creation_date"]).days
  except:
    whois_return = 1 
    whois_days = 0
  
  return favicon_return,anchor_return,whois_return, whois_days

#https://github.com/himanshi18037/WhatAPhish/blob/main/Features_For_New_DataPoint.ipynb 
def check_favicon(url):
  try :
    extract_res = tldextract.extract(url)
    url_ref = extract_res.domain

    favs = favicon.get(url,timeout=2)
    match = 0
    for favi in favs:
      url2 = favi.url
      extract_res = tldextract.extract(url2)
      url_ref2 = extract_res.domain

      if url_ref in url_ref2:
        match += 1

    if match >= len(favs)/2:
      return 0
    return 1
  except :
    return 0

def check_dns_record(url):
  extract_res = tldextract.extract(url)
  url_ref = extract_res.domain + "." + extract_res.suffix
  try:
    _ = whois.whois(url)
    return 0
  except:
    return 1

#Age of Domain
#https://github.com/himanshi18037/WhatAPhish/blob/main/Features_For_New_DataPoint.ipynb  
def check_age_of_domain(url):
  extract_res = tldextract.extract(url)
  url_ref = extract_res.domain + "." + extract_res.suffix
  try:
    whois_res = whois.whois(url_ref)
    return str((datetime.datetime.now() - whois_res["creation_date"]).days)
  except:
    return 0
#https://github.com/himanshi18037/WhatAPhish/blob/main/Features_For_New_DataPoint.ipynb 
def iframe_mouseover_rightclick(url):
  try:
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    if str(soup.iframe).lower().find("frameborder") == -1:
      iframe_return = 0
    else :
      iframe_return = 1
    if str(soup).lower().find('onmouseover="window.status') != -1:
      mouseover_return = 1
    else :
      mouseover_return = 0
    
    if str(soup).lower().find("preventdefault()") != -1:
      rightclick_return = 1
    elif str(soup).lower().find("event.button == 2") != -1:
      rightclick_return =  1
    else :
      rightclick_return = 0
    return iframe_return, mouseover_return, rightclick_return
  except :
    return 0,1,0

def check_iframe(url):
  try:
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    if str(soup.iframe).lower().find("frameborder") == -1:
      return 0
    return 1
  except :
    return 0

def check_onmouseover(url):
  try:
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    if str(soup).lower().find('onmouseover="window.status') != -1:
      return 1
    return 0
  except:
    return 1

def check_rightclick(url):
  try :
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    if str(soup).lower().find("preventdefault()") != -1:
      return 1
    elif str(soup).lower().find("event.button == 2") != -1:
      return 1
    return 0
  except :
    return 0

#https://stackoverflow.com/questions/41620369/how-to-get-ssl-certificate-details-using-python
def check_ssl(hostname):
  try:
    ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'
    context = ssl.create_default_context()
    context.check_hostname = False

    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 5 second timeout
    conn.settimeout(5.0)
    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    
    now = datetime.datetime.now()
    expire = datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)
    diff = expire - now
    return 1, diff.days
  except:
    return 0 , -1

#https://www.geeksforgeeks.org/ssl-certificate-verification-python-requests/
def find_valid_certificate(url):
  try :
      r = requests.get(url, allow_redirects=False, timeout = 2)
      return 1
  except :
      return 0

#url_shortened
def shortened_redirects(url):
  try :
    response = requests.head(url, allow_redirects=True)
    if response.status_code == 200  and response.url != url : #url returned != url send
      return  1 , response.url , len(response.history)
    else :
      return 0, None , 0
  except:
    return 0, None , 0

def check_https(url):
    return 1 if 'https' in url else 0
#https://github.com/himanshi18037/WhatAPhish/blob/main/Features_For_New_DataPoint.ipynb   
def sfh(u):
    try:
        programhtml = requests.get(u).text
        s = BeautifulSoup(programhtml,"lxml")
        f = str(s.form)
        ac = f.find("action")
        if(ac!=-1):
            i1 = f[ac:].find(">")
            u1 = f[ac+8:i1-1]
            if(u1=="" or u1=="about:blank"):
                return 1
            er1 = tldextract.extract(u)
            upage = erl.domain
            erl2 = tldextract.extract(u1)
            usfh = erl2.domain
            if upage in usfh:
                return 0
            return 1
        else:
            # Check this point
            return 0
    except:
        # Check this point
        return 0
    
#https://github.com/himanshi18037/WhatAPhish/blob/main/Features_For_New_DataPoint.ipynb 
def url_validator(url):
    try:
        result = urlparse(url)
        return 1 if all([result.scheme, result.netloc, result.path]) else 0
    except:
        return 0

def check_headers(url):
  try :
    r = requests.get(url).headers
    try:
      cookie = 1 if r['Set-Cookie'] != None else 0
    except :
      cookie = 0

    try:
      strict_trans_sec = 1 if r['Strict-Transport-Security'] != None else 0
    except :
      strict_trans_sec = 0
    
    return cookie, strict_trans_sec
  except :
    return 0,0
  
def find_page_counters(url):
  try:
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content.lower(), "lxml")
    a_tags = soup.find_all('a')
    div_tags = soup.find_all('div')
    pop_up_count = 0
    for a in a_tags :
      if 'pop up' in a:
        pop_up_count += 1
    for div in div_tags :
      if 'pop up' in div:
        pop_up_count += 1
    a_tags_count = len(a_tags)
    form_tags_count = len(soup.find_all('form'))
    email_tags_count = len(soup.find_all(string=re.compile('email')))
    pass_tags_count = len(soup.find_all(string=re.compile('password')))
    hidden_tags_count = len(soup.find_all(string=re.compile('hidden')))
    actions_tags_count = len(soup.find_all(string=re.compile('action')))
    signin_tags_count = len(soup.find_all(string=re.compile('sign in')))
    signup_tags_count = len(soup.find_all(string=re.compile('sign up')))
    return a_tags_count,form_tags_count,email_tags_count,pass_tags_count,hidden_tags_count,actions_tags_count,pop_up_count,signin_tags_count,signup_tags_count
  except :
    return 0,0,0,0,0,0,0,0,0

#URL of Anchor
#https://github.com/himanshi18037/WhatAPhish/blob/main/Features_For_New_DataPoint.ipynb 
def check_URL_of_anchor(url):
  try :
    extract_res = tldextract.extract(url)
    url_ref = extract_res.domain
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    a_tags = soup.find_all('a')
    if len(a_tags) == 0:
      return 0
    
    invalid = ['#', '#content', '#skip', 'JavaScript::void(0)']
    bad_count = 0
    for t in a_tags:
      link = t['href']

      if link in invalid:
        bad_count += 1

      if url_validator(link):
        extract_res = tldextract.extract(link)
        url_ref2 = extract_res.domain

        if url_ref not in url_ref2:
          bad_count += 1

    bad_count /= len(a_tags)
  
    return bad_count
  except :
    return -1

def replace_params(params):
  return params.replace('%20',' ').\
                replace('%21','!').\
                replace('%22','"').\
                replace('%23','#').\
                replace('%24','$').\
                replace('%25','%').\
                replace('%26','&').\
                replace('%27',"'").\
                replace('%28','(').\
                replace('%29',')').\
                replace('%2A','*').\
                replace('%2B','+').\
                replace('%2b','+').\
                replace('%2C',',').\
                replace('%2c',',').\
                replace('%2D','-').\
                replace('%2d','-').\
                replace('%2E','.').\
                replace('%2e','.').\
                replace('%2F','/').\
                replace('%2f','/').\
                replace('%3A',':').\
                replace('%3a',':').\
                replace('%3B',';').\
                replace('%3b',';').\
                replace('%3C','<').\
                replace('%3c','<').\
                replace('%3D','=').\
                replace('%3d','=').\
                replace('%3E','>').\
                replace('%3e','>').\
                replace('%3F','?').\
                replace('%3fF','?').\
                replace('&amp;','&')

def extract_features(url):
  #Check if url exists and is active
  url_new, is_active = check_active_url(url,2) #2 seconds timeout
  if not is_active or url_new == None :
    return None
  features_extracted = [0]*63
  phStatus, expanded, num_redirects = shortened_redirects(url)
  features_extracted[1] = num_redirects #qnt_redirects
  features_extracted[2] = phStatus #url_shortened
  if expanded is not None :
    if len(expanded) >= len(url):
      url = expanded
  
  parsed_url = urlparse(url)
  extract_res = tldextract.extract(url)
  TLD = extract_res.suffix
  if url.startswith('http'):
    domain = parsed_url.netloc
  else :
    domain = extract_res.domain + '.' + extract_res.suffix
  
  #scheme = parsed_url.scheme
  path = parsed_url.path.split('/')
  directory = '/'.join(path[:-1])
  filename = path[-1]
  params = replace_params(parsed_url.query)
  
  features_extracted[3],features_extracted[8],features_extracted[4],features_extracted[30] = favicon_anchor_whois_days(url)  #favicon, anchor, whois
  #features_extracted[4] = check_dns_record(url)  #dns record
  #iframe_return, mouseover_return, rightclick_return
  features_extracted[5],features_extracted[7],features_extracted[6] = iframe_mouseover_rightclick(url)  #iFrame,onmouseover,rightClick
  #features_extracted[6] = check_rightclick(url)  #rightClick
  #features_extracted[7] = check_onmouseover(url)  #onmouseover
  #features_extracted[8] = check_URL_of_anchor(url)  #check_URL_of_anchor
  features_extracted[9] = sfh(url)  #sfh

  #TABLE 1
  features_extracted[10] = double_slash(url)
  features_extracted[11] = count_signs(url,'.')  #count . in url
  features_extracted[12] = count_signs(url,'-')  #count - in url
  features_extracted[13] = count_signs(url,'?')  #count ? in url
  features_extracted[14] = count_signs(url,'@')  #count @ in url
  features_extracted[15] = count_signs(url,'#')  #count # in url
  features_extracted[16] = count_signs(url,'$')  #count $ in url
  features_extracted[17] = count_signs(url,'%')  #count % in url
  features_extracted[18] = len(TLD)  #TLD length
  features_extracted[19] = len(TLD.split('.')) #TLD count
  features_extracted[20] = len(url)  #URL length
  features_extracted[21] = email_in_url(url)  #email in url
  features_extracted[22] = scriptInUrl(url) #word script in url
  features_extracted[23] = check_https(url) #check https in url

  #TABLE 2
  features_extracted[24] = count_signs(domain,'.')  #count . in domain
  features_extracted[25] = count_signs(domain,'-')  #count - in domain
  features_extracted[26] = count_vowels(domain)  #count vowels
  features_extracted[27] = len(domain)  #Domain length
  features_extracted[28] = domain_ip(domain)  #Ip in domain
  features_extracted[29] = client_server(domain)  #Client or Server in domain
  #features_extracted[30] = check_age_of_domain(domain)
  features_extracted[0], features_extracted[31] = check_ssl(domain) # Valid certificate and days till expiration 

  #Table 3 
  features_extracted[32] = count_signs(directory,'.')  #count . in directory
  features_extracted[33] = count_signs(directory,'-')  #count - in directory
  features_extracted[34] = count_signs(directory,'@')  #count @ in directory
  features_extracted[35] = count_signs(directory,'/')  #count / in directory
  features_extracted[36] = count_signs(directory,'#')  #count # in directory
  features_extracted[37] = len(directory)  #Domain length

  #Table 4
  features_extracted[38] = count_signs(filename,'.')  #count . in File
  features_extracted[39] = count_signs(filename,'-')  #count - in File
  features_extracted[40] = count_signs(filename,'@')  #count @ in File
  features_extracted[41] = count_signs(filename,'%')  #count % in File
  features_extracted[42] = len(filename)  #File length

  #Table 5
  features_extracted[43] = count_signs(params,'.')  #count . in params
  features_extracted[44] = count_signs(params,'-')  #count - in params
  features_extracted[45] = count_signs(params,'@')  #count @ in params
  features_extracted[46] = count_signs(params,'_')  #count _ in params
  features_extracted[47] = count_signs(params,'#')  #count # in params
  features_extracted[48] = count_signs(params,'$')  #count $ in params
  features_extracted[49] = count_signs(params,'%')  #count % in params
  features_extracted[50] = len(params)  #params length
  features_extracted[51] = tld_in_params(params)  #tld in params
  features_extracted[52] = count_params(params)   #number of parameters

  cookie, strict_trans_sec = check_headers(url) #cookie, strict_trans_sec
  features_extracted[53] = cookie
  features_extracted[54] = strict_trans_sec
  a,b,c,d,e,f,g,h,i = find_page_counters(url) #a_tags_count,form_tags_count,email_tags_count,pass_tags_count,hidden_tags_count,actions_tags_count,pop_up_count,signin_tags_count,signup_tags_count
  features_extracted[55] = a
  features_extracted[56] = b
  features_extracted[57] = c
  features_extracted[58] = d
  features_extracted[59] = e
  features_extracted[60] = f
  # OUT features_extracted[69] = g
  features_extracted[61] = h
  features_extracted[62] = i
  return features_extracted

if __name__ == '__main__':
  print(extract_features('https://onlinebanking.bancogalicia.com.ar/login'))
