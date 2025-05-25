from feelbot.format.text_renderer import flatten_result, render_cli

def print_result(result: dict) -> None:
    flat = flatten_result(result)
    print(render_cli(flat))
