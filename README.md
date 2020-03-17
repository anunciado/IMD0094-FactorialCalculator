# Factorial Calculator
A factorial calculator using redis as cache.

## Installation

### System requirements

gafes has the following system requirements:
* [Python (>=3.5)](https://www.python.org/downloads/)
* [walrus (>=0.8.0)](https://pypi.org/project/walrus/)
* [redis (>=5.0.8)](https://redis.io/)


### Installing 

Please install all dependencies manually with:

```
curl https://raw.githubusercontent.com/anunciado/IMD0094-FactorialCalculator/master/requirements.txt | xargs -n 1 -L 1 pip install
```
For redis, i suggest the use of [Docker](https://docs.docker.com/install/).

### Running

There are two ways to run the program:

* Compile the IDE (PyCharm - Python IDE):
1. Just open the IDE
2. Import the project folder as a Project
3. Select Run/Debug Configurations and add the following parameters:
```
-a <adress> -p <port>
```
An example would be:
```
-a localhost -p 9090
```
4. Choose Run calculator on the context menu.
5. From this it only interacts with the system.

* Compile by terminal:
1. Enter the src folder and run the following command:
```
python main.py -a <adress> -p <port>
```
An example would be:
```
python main.py -a localhost -p 9090
```
2. From this it only interacts with the system.

## Built With

* [Atom](https://atom.io/) - A text editor used

## Authors
### Developers: 
* **Luís Eduardo Anunciado Silva ([cruxiu@ufrn.edu.br](mailto:cruxiu@ufrn.edu.br))** 
### Project Advisor: 
* **Gustavo Bezerra Paz Leitao ([gustavo.leitao@imd.ufrn.br](mailto:gustavo.leitao@imd.ufrn.br))**

See also the list of [contributors](https://github.com/anunciado/IMD0094-FactorialCalculator/contributors) who participated in this project.

## License

This project is licensed under the MIT - see the [LICENSE](LICENSE) file for details

## Contributing

Feel free to fork the repository, add your changes and give back by issuing a pull request.


