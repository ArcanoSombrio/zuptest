# language:pt
# file:remove_product_from_cart.feature
# -- FILE: steps\remove_product_from_cart.py

@Google
Funcionalidade: Remover produto do carrinho @remove_product
  Cenario: Realizar remoção de produto no carrinho no portal americanas @remove_product
    Dado que eu esteja com a home do portal americanas aberto @remove_product
    Quando eu inserir o código do produto no campo de busca @remove_product
      E clicar no botão de busca @remove_product
    Entao a pesquisa é realizada e o produto corespondente é exibido na lista @remove_product
      E selecionar o produto @remove_product
    Então a página com as informações para compra do produto é exibida @remove_product
      E validar as informações do produto @remove_product
      E clicar em comprar @remove_product
    Então a página de seleção da garantia e do seguro é exibida @remove_product
      E clicar em continuar @remove_product
    Então a página do carrinho de compras é exibida com o produto adicionado @remove_product
      E validar as informações do produto no carrinho de compras @remove_product
      E clicar em remover @remove_product
    Então o produto é removido do carrinho de compras @remove_product
     E é exibida uma mensagem informando que nã há produtos no carrinho de compras @remove_product
