# Операции с строками

s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed libero tellus, luctus ultricies ultrices at, aliquam in odio. Fusce mattis sem id mauris consectetur, non pellentesque leo sagittis. In fringilla id odio vitae ullamcorper. Integer et mi turpis. Duis posuere dapibus lectus ut bibendum. Sed non turpis faucibus, viverra tortor nec, dignissim magna. Nunc vitae gravida nibh. Vestibulum vestibulum auctor ligula non pretium. Sed nisi felis, ultrices ac venenatis sit amet, vestibulum quis purus. Donec efficitur quam nec condimentum lacinia. Sed quis maximus libero, nec auctor justo. Nullam id justo eget purus imperdiet fringilla sit amet id dolor. Sed risus dui, malesuada quis massa eu, laoreet varius ligula. Morbi laoreet ornare nulla ut tincidunt. Vestibulum aliquet consequat tortor ornare consequat. Morbi et suscipit nisl. Pellentesque pellentesque quam magna, in scelerisque tortor suscipit a. Cras enim mauris, ultrices sollicitudin libero a, dignissim rhoncus lacus. Vestibulum sed porttitor arcu. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Duis vitae lorem purus. Quisque interdum dui lorem, eget gravida orci porttitor eu. Quisque sed magna sed libero pharetra volutpat at in quam. Nullam placerat et magna a maximus. Nam blandit ante ut urna sagittis, sit amet luctus quam fringilla. Aliquam erat volutpat. Fusce faucibus scelerisque dolor in consectetur. Duis rutrum maximus porttitor. sollicitudin laoreet pharetra. Sed diam odio, scelerisque sit amet turpis eget, sollicitudin luctus quam. Ut vestibulum, nibh non ullamcorper bibendum, metus nibh porttitor diam, ut fringilla dolor libero non tortor. Quisque id felis quis nisl pharetra fringilla posuere quis diam. Duis vehicula vitae urna et suscipit. Ut et vehicula mauris. Sed eget laoreet mi, eget venenatis urna. Vivamus id maximus nulla. Curabitur eu pellentesque sapien. uis efficitur quam id est porttitor, id ornare tortor accumsan. Integer feugiat cursus tellus nec malesuada. Nullam ac mauris in tellus accumsan rhoncus. Nulla consectetur diam vel nibh iaculis, vel efficitur leo egestas. Fusce pulvinar, felis sed condimentum accumsan, leo orci volutpat massa, sed interdum nisl justo quis urna. Proin sit amet lectus eu est congue finibus sed et ex. Aenean vel tortor eget eros malesuada hendrerit ut lacinia ligula. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin vel laoreet lectus. Praesent maximus luctus odio, a vehicula dui pulvinar ullamcorper. Nam ac urna egestas, fringilla quam in, laoreet enim. Donec enim sem, tempus sit amet tincidunt a, mattis a purus. Praesent et lorem erat. In eu elit nec dolor sodales dapibus. Vivamus vestibulum condimentum nunc in viverra. Ut aliquet convallis libero et dictum. Nullam eu faucibus est. Duis nec maximus ex. Vestibulum scelerisque vehicula tortor eu dignissim. Nam libero justo, suscipit ut pretium sed, laoreet a arcu. Phasellus tincidunt congue tortor, eget sodales lacus dictum sit amet. Phasellus scelerisque lobortis pulvinar. Praesent vitae orci diam. Phasellus orci velit, commodo a nibh et, pulvinar efficitur risus. Quisque commodo mauris urna, et fermentum orci maximus a."

print(s)

# первый симв.
print(s[0])

# длина строки
print('len str: ', len(s))

# посл. симв. в строке
print('len str: ', s[len(s) - 1])

# посл. симв. в строке
print(s[-1])

# срез из 10 первых симв.
print(s[:10])

# срез из 10 симв. начиная с 10
print(s[10:20])

# срез из 10 симв. начиная с 10 и взять каждый 3 симв.
print(s[10:20:3])

# срез каждый 3 симв. в строке
print(s[::3])


# не сработает, т.к. строка не изменяемый тип данных
# s[0] = 'asdasd'

# конкатенация строк
s1 = '11111' + 'as das dasd'
print(s1)

# Заменить первый симв. в строке s на строку s1
s = s1 + s[1:]
print(s)

# создание строки из списка, по раздел. " "(пробел)
l = ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'of']
s2 = ' '.join(l)
print(s2)

# разбить строку s по раздел. "."(точка)
l2 = s.split('.')
print(l2)

# удаление пробелов с начала строки(lstrip) и конца(rstrip)
s3 = ' Hello, John! '
print(s3, 'len: ', len(s3))
s3 = s3.lstrip()
print(s3, 'len: ', len(s3))
s3 = s3.rstrip()
print(s3, 'len: ', len(s3))

# изменить регистр 
s4 = 'nam libero'
print(s4.upper())

s5 = 'LOREM IPSUM'
print(s5.lower())

s6 = 'lorem ipsum dolor sit amet, consectetur adipiscing elit'

# Lorem ipsum dolor sit amet, consectetur adipiscing elit

