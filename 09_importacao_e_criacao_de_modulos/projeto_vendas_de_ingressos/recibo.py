#criando módulo de recibo
import datetime

def gerar_recibo(nome, evento, quantidade, total):
    data_compra = datetime.datetime.now()

    recibo = f"""
========== RECIBO ========= 

Cliente: {nome}
Evento: {evento}
Ingressos: {quantidade}
Total R$: {total:2f}
Data: {data_compra}

===========================

"""
    return recibo