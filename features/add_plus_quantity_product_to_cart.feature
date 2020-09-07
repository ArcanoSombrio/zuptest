# language:pt
# file:add_plus_quantity_product_to_cart.feature
# -- FILE: steps\add_plus_quantity_product_to_cart.py

@Google
Funcionalidade: Adicionar produto ao carrinho de compras e incrementar quantidade @add_product_plus
  Cenario: Realizar adição de produto ao carrinho de compras no portal americanas e incrementar a quantidade @add_product_plus
    Dado que eu esteja com a home do portal americanas aberto @add_product_plus
    Quando eu inserir o código do produto no campo de busca @add_product_plus
      E clicar no botão de busca @add_product_plus
    Entao a pesquisa é realizada e o produto corespondente é exibido na lista @add_product_plus
      E selecionar o produto @add_product_plus
    Então a página com as informações para compra do produto é exibida @add_product_plus
      E validar as informações do produto @add_product_plus
      E clicar em comprar @add_product_plus
    Então a página de seleção da garantia e do seguro é exibida @add_product_plus
      E clicar em continuar @add_product_plus
    Então a página do carrinho de compras é exibida com o produto adicionado @add_product_plus
      E validar as informações do produto no carrinho de compras @add_product_plus
      E clicar no botão de + para incrementa a quantidade do produto no carrinho @add_product_plus
    Então as informações são atualizadas @add_product_plus
      E validar as novas informações do produto no carrinho @add_product_plus
