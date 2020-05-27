# automv

automv is a tool to automate moving files by rules, inspired by [Spotless](https://lightpillar.com/spotless.html)

## Installation

```bash
git clone https://github.com/zhangchi0104/automv.git
```

## Usage

```bash
# config the config.json

# General cases
python3 main.py file
```

## TODO

- [X] add priorties to rule
- [ ] be able to specify a rule
- [ ] be able to nested rules
- [X] be able to process multiple files
- [ ] add more conditions and matchers 
    - [X] added `any` matcher and `extension` condition
- [ ] add pre moving and post moving tasks
- [ ] add pytest 
- [ ] dump rules by `pickle` for better performance
- [ ] rewrite this project in other language

## Changelog
###
- now iterate through all the rules based on priority
- updated docs
- it can process multiple files

### v0.0.1 
- Project created 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)