To co zrobiłem to:
1) wczytywanie słownika
2) dla każdego słowa wyciągania 2- 3- 4- słowogramów kończących sie na samogloske
3) zliczanie wsystąpień tych słowogramów
4) utworzenie słownika który jako klucz ma te słowogramy a jako wartość ich ilość częstość wystąpień
5) z racji że przeglądnięcie całego słownika zajmuje chwilę czasu - przy pierwszym uruchomieniu zapisywany jest dict_pickle.pkl z wynikiem zliczania sylab


tam masz zakomentowaną linijkę z wykorzystaniem biblioteki do tworzenia generatora wartości o danej dystrybucji - obczaj co i jak - powinno być bez problemu

Trzeba dorobić
1) wczytywanie z linii poleceń długości hasła do wygenerowania
2) generowanie tego hasła
3) wygenerowanie jakiejś paczki pytonowej, tak żeby wynikowo był jeden plik (a nie tak jak teraz skrypt + slowa.txt)