import gradio as gr

def parse_input(text):
    stops = []
    lines = text.strip().split("\n")
    for line in lines:
        if not line.strip():
            continue
        parts = line.split(",")
        if len(parts) != 2:
            raise ValueError("Each line must be: Stop Name, Crowd Count")
        name = parts[0].strip()
        crowd = int(parts[1].strip())
        stops.append({"stop_name": name, "crowd_count": crowd})
    return stops

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["crowd_count"] >= right[j]["crowd_count"]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def sort_stops(text):
    try:
        stops = parse_input(text)
        if not stops:
            return "Please enter at least one shuttle stop."

        sorted_stops = merge_sort(stops)

        result = "Sorted Shuttle Stops (Highest crowd first):\n\n"
        for i, stop in enumerate(sorted_stops, start=1):
            result += f"{i}. {stop['stop_name']} - {stop['crowd_count']}\n"

        result += f"\nSend the extra shuttle to: {sorted_stops[0]['stop_name']}"
        return result

    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as app:
    gr.Markdown("# Campus Shuttle Crowd Sorter")
    gr.Markdown("Enter one shuttle stop per line in this format: Stop Name, Crowd Count")

    input_box = gr.Textbox(
        label="Shuttle Stop Data",
        lines=8,
        placeholder="Library,42\nMain Hall,15\nResidence,67"
    )

    output_box = gr.Textbox(label="Sorted Results", lines=12)

    sort_button = gr.Button("Sort Stops")

    sort_button.click(fn=sort_stops, inputs=input_box, outputs=output_box)

app.launch()
