# Creates a table from a list of data points
def render_table(data_points):
    counter = 1

    output = "<table class='data-table'>\n"

    # Iterate over the data_points list
    for data in data_points:
        # Create a row
        row = "<tr>\n"

        row += "<td>{}</td>\n".format(counter)
        row += "<td>{}</td>\n".format(data)

        # Finish the row element
        row = row + "</tr>\n"

        # increment counter and add row to the output
        counter += 1
        output += row

    output += "</table>\n"

    return output