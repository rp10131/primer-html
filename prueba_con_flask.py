from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    mensaje = '<a href="/random_fact">¡Ver un dato aleatorio!</a> o <a href="/contraseña">¡Generar una contraseña!</a>'
    return mensaje

@app.route("/random_fact")
def random_fact():
    facts_list = ['La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos', 'Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.',
            'El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna',
            'Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo',
            'Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo',
            'Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos',
            'Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos',
            'Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas'
]

    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/contraseña")
def generador_c():
    """Genera una contraseña aleatoria de 6 a 20 caracteres"""
    caracteres = "+-_'/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contrs = ''

    x = random.randint(6,20)

    for i in range(x):
        carácter_aleatorio = random.choice(caracteres)
        contrs += carácter_aleatorio
        
    return f'<p>Se generó esta contraseña de {x} caracteres: {contrs}</p>'

app.run(debug=True)
