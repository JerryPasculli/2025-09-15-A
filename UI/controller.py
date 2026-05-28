import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self,e):
        self._view.txt_result.controls.clear()
        anno1 = self._view._ddAnno1.value
        anno2 = self._view._ddAnno2.value
        if anno1 is None or anno2 is None or anno1 >anno2:
            t1 = ft.Text("NON HAI SCELTO UN RANGE DI ANNI COERENTI", color = "red")
            self._view.txt_result.controls.append(t1)
            self._view.update_page()
            return
        t1, t2 = self._model.creaGrafo(int(anno1), int(anno2))
        t1 = ft.Text(t1, color="red")
        t2 = ft.Text(t2)
        self._view.txt_result.controls.append(t1)
        self._view.txt_result.controls.append(t2)
        self._view._btnstampa.disabled = False
        self._view.update_page()
    def handleDettagli(self, e):
        t1, t2 = self._model.dettagliPeso()
        t1 = ft.Text(t1, color="red")
        t2 = ft.Text(t2)
        self._view.txt_result.controls.append(t1)
        self._view.txt_result.controls.append(t2)
        t1, t2 = self._model.dettagliComp1()
        t1 = ft.Text(t1, color="red")
        t2 = ft.Text(t2)
        self._view.txt_result.controls.append(t1)
        self._view.txt_result.controls.append(t2)
        t1, t2 = self._model.dettagliComp2()
        t1 = ft.Text(t1, color="red")
        t2 = ft.Text(t2)
        self._view.txt_result.controls.append(t1)
        self._view.txt_result.controls.append(t2)
        self._view.update_page()
    def handleCerca(self, e):
        self._view.txt_result.controls.clear()
        numero = self._view._txtInK.value
        try:
            int(numero)
        except:
            t1 = ft.Text("NON HAI SCELTO UN NUMERO DI PILOTI COERENTI", color="red")
            self._view.txt_result.controls.append(t1)
            self._view.update_page()
            return
        numero = int(numero)
        if numero == 1 or numero == 0:
            t1 = ft.Text("NON HAI SCELTO UN NUMERO DI PILOTI COERENTI: 1 o 0 non sono ammissibili", color="red")
            self._view.txt_result.controls.append(t1)
            self._view.update_page()
            return
        t1 = self._model.cammino(numero)
        t1 = ft.Text(t1)
        self._view.txt_result.controls.append(t1)
        self._view.update_page()


    def popola(self):
        lista = self._model.popola()
        for element in lista:
            opzione = ft.dropdown.Option(element)
            self._view._ddAnno1.options.append(opzione)
            self._view._ddAnno2.options.append(opzione)
        self._view.update_page()

