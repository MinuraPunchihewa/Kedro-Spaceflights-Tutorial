# Kedro Spaceflights Tutorial

This is an implementation of the Kedro Spaceflights Tutorial.

## Run Locally

Clone the project,

```
git clone https://github.com/MinuraPunchihewa/kedro-spaceflights.git
```

Go to the project directory,

```
cd kedro-spaceflights
```

Install dependencies,

```
kedro install
```

Run the default pipeline,

```
kedro run
```

To run a pipeline of choice,
```
kedro run --pipeline <pipeline_name>
```

## Testing

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

## Related Projects

- [Kedro Spaceflights Starter](https://github.com/quantumblacklabs/kedro-starter-spaceflights): The Kedro Spaceflights Starter Project.
