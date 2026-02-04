$(document).ready(function () {
//   $("#btn-chart-fullscreen").on("click", function () {
//     $("#fulscreen-modal").show();
//     chartBarplot(null, "#emp-comp-chart-fullscreen");
//   });

//   tabulator_table = new Tabulator("#tabulator-table", {
//     // data:data_title,
//     pagination: "local",
//     paginationSize: 10,
//     paginationSizeSelector: [10, 25, 50, 100],
//     // responsiveLayout:"collapse",
//     height: 600,
//     layout: "fitDataTable",
//     columns: [
//       { title: "Id", field: "ids", titleDownload: "Id" },
//       {
//         title: "<i class='fas fa-calendar-alt'></i>&nbsp; Year",
//         field: "fiscal_year",
//         titleDownload: "Fiscal Year",
//       },
//       {
//         title: "<i class='fas fa-landmark'></i>&nbsp;Entity",
//         field: "entity_name",
//         titleDownload: "Entity",
//       },
//       {
//         title: "<i class='fas fa-user'></i>&nbsp;Employee</th>",
//         field: "employee_name",
//         titleDownload: "Employee",
//       },
//       {
//         title: "<i class='fas fa-briefcase'></i>&nbsp;Title",
//         field: "title",
//         titleDownload: "Title",
//       },
//       {
//         title: "<i class='fas fa-dollar-sign'></i>&nbsp;Wages",
//         field: "wages",
//         formatter: "money",
//         titleDownload: "Wages",
//         formatterParams: {
//           decimal: ".",
//           thousand: ",",
//           symbol: "$",
//           precision: 2,
//         },
//       },
//       {
//         title: "<i class='fas fa-dollar-sign'></i>&nbsp;Benefits",
//         field: "benefits",
//         formatter: "money",
//         titleDownload: "Benefits",
//         formatterParams: {
//           decimal: ".",
//           thousand: ",",
//           symbol: "$",
//           precision: 2,
//         },
//       },
//       {
//         title: "<i class='fas fa-dollar-sign'></i>&nbsp;Total",
//         field: "total",
//         formatter: "money",
//         titleDownload: "Total ",
//         formatterParams: {
//           decimal: ".",
//           thousand: ",",
//           symbol: "$",
//           precision: 2,
//         },
//       },
//     ],
//   });

  // Update the download buttons to listen for clicks so they can download the data to the users device

  //trigger download of data.csv file
  // $("#download-csv").on("click", function () {
  //   tabulator_table.download("csv", "data.csv");
  // });

  // //trigger download of data.json file
  // $("#download-json").on("click", function () {
  //   tabulator_table.download("json", "data.json");
  // });

  // //trigger download of data.xlsx file
  // $("#download-xlsx").on("click", function () {
  //   tabulator_table.download("xlsx", "data.xlsx", { sheetName: "My Data" });
  // });

  // //trigger download of data.pdf file
  // $("#download-html").on("click", function () {
  //   tabulator_table.download("html", "data.html", { style: true });
  // });

//   $("#btn-chart-download").on("click", function () {
//     var svgElement = $("#emp-comp-chart").children("div").children("svg")[0];
//     var simg = new Simg(svgElement);
//     // Replace the current SVG with an image version of it.
//     simg.replace();
//     // And trigger a download of the rendered image.
//     simg.download();

//     // Since the canvas is now a png, we need to redraw it to have interactivity again. lmao :/
//     chartBarplot(null, "#emp-comp-chart");
//   });

//   $("btn-chart-fullscreen-download").on("click", function () {
//     var svgElement = $("#emp-comp-chart-fullscreen").children("svg")[0];
//     var simg = new Simg(svgElement);
//     // Replace the current SVG with an image version of it.
//     simg.replace();
//     // And trigger a download of the rendered image.
//     simg.download();

//     // Since the canvas is now a png, we need to redraw it to have interactivity again. lmao :/
//     chartBarplot(null, "#emp-comp-chart-fullscreen");
//   });
});

// $(window).resize(function () {
//   if (this.resizeTO) clearTimeout(this.resizeTO);
//   this.resizeTO = setTimeout(function () {
//     chartBarplot(null, "#emp-comp-chart");
//   }, 500);
// });

// Create a "listener" for the fiscal year object. When the fiscal year select input is changed, we tell it to update the chart.
window.fiscal_years_selected = {
  fiscalYearInternal: [],
  fiscalYearListener: function (val) {},
  set fiscal_years(val) {
    this.fiscalYearInternal = val;
    this.fiscalYearListener(val);
  },
  get fiscal_years() {
    return this.fiscalYearInternal;
  },
  registerListener: function (listener) {
    this.fiscalYearListener = listener;
  },
};

fiscal_years_selected.registerListener(function (val) {
  //Do remake the plot
  // console.log("fiscal years"+val)
  if (window.mostRecentRawResult.length > 0) {
    updateData();
  }
});

window.entities_selected = {
  entityInternal: [],
  entityListener: function (val) {},
  set entities(val) {
    this.entityInternal = val;
    this.entityListener(val);
  },
  get entities() {
    return this.entityInternal;
  },
  registerListener: function (listener) {
    this.entityListener = listener;
  },
};

entities_selected.registerListener(function (val) {
  //Do remake the plot
  // console.log("entities "+val)
  if (window.mostRecentRawResult.length > 0) {
    updateData();
  }
});

window.employees_selected = {
  employeeInternal: [],
  employeeListener: function (val) {},
  set employees(val) {
    this.employeeInternal = val;
    this.employeeListener(val);
  },
  get employees() {
    return this.employeeInternal;
  },
  registerListener: function (listener) {
    this.employeeListener = listener;
  },
};

employees_selected.registerListener(function (val) {
  //Do remake the plot
  // console.log("employees "+val)
  if (window.mostRecentRawResult.length > 0) {
    updateData();
  }
});

window.titles_selected = {
  titleInternal: [],
  titleListener: function (val) {},
  set titles(val) {
    this.titleInternal = val;
    this.titleListener(val);
  },
  get titles() {
    return this.titleInternal;
  },
  registerListener: function (listener) {
    this.titleListener = listener;
  },
};

titles_selected.registerListener(function (val) {
  //Do remake the plot
  // console.log("titles "+val)
  if (window.mostRecentRawResult.length > 0) {
    updateData();
  }
});

function lookupData(me) {
  var nm = document.getElementById("emp-search-input").value.trim();

  if (nm.length == 0) {
    window.alert("Must enter a name.");
    return;
  }

  // package them up
  var obj = Object();
  obj["name"] = nm;
  SendQueryJson("getEmployeeSearch", obj, makePage, obj);
}

function makePage(data, obj) {
  createFilters(data, obj);
  updateData();
}

function createFilters(vals, obj) {
  // 1. Get the new options
  var newGovernmentTypeOptions = [];
  var newFiscalYearOptions = [];
  var newEntityOptions = [];
  var newEmployeeOptions = [];
  var newTitleOptions = [];
  for (var i = 0; i < vals.length; i++) {
    newFiscalYearOptions[i] = vals[i].fiscal_year;
    newEntityOptions[i] = vals[i].entity_name;
    newTitleOptions[i] = vals[i].title;
    newEmployeeOptions[i] = vals[i].employee_name;
  }

  // B. Update the fiscal year filter options 

  start_time = performance.now();
  // 2. Filter to only the unique options
  newFiscalYearOptionsUQ = newFiscalYearOptions
    .filter((item, i, ar) => ar.indexOf(item) === i)
    .sort();
  // console.log(newFiscalYearOptionsUQ);

  // 3. Update the select input
  var $temp_fiscal_year_filter = $("#fiscal-year-filter");

  // 3.1 Empty the old filter's options
  $temp_fiscal_year_filter.empty();

  // 3.2 Loop through the new unique options and append them as options to the select input
  $.each(newFiscalYearOptionsUQ, function (key, value) {
    $temp_fiscal_year_filter.append(
      $("<option></option>").attr("value", value).text(value)
    );
  });

  // 3.3 Refresh/repaint the select picker so that the new options are visible.
  $("#fiscal-year-filter").selectpicker("refresh");

  //C. Update the Entity options
  // 2. Filter to only the unique options
  // newEntityOptionsUQ = newEntityOptions.filter((item, i, ar) => ar.indexOf(item) === i).sort();
  let newEntityOptionsUQ = [...new Set(newEntityOptions)].sort();

  // 3. Update the select input
  var $temp_entity_filter = $("#entity-filter");

  // 3.1 Empty the old filter's options
  $temp_entity_filter.empty(); // remove old options

  // 3.2 Loop through the new unique options and append them as options to the select input
  $.each(newEntityOptionsUQ, function (key, value) {
    $temp_entity_filter.append(
      $("<option></option>").attr("value", value).text(value)
    );
  });

  // 3.3 Refresh/repaint the select picker so that the new options are visible.
  $("#entity-filter").selectpicker("refresh");

  //D. Update the Employee filter options

  // start_time = performance.now()
  // 2. Filter to only the unique options
  // newEmployeeOptionsUQ = newEmployeeOptions.filter((item, i, ar) => ar.indexOf(item) === i).sort();
  // start_map_time = performance.now()
  let newEmployeeOptionsUQ = [...new Set(newEmployeeOptions)].sort();
  // end_time = performance.now()
  // console.log( 'newEmployeeOptionsUQ SET filter - benchmark:')
  // console.log(end_time - start_map_time)
  // 3. Update the select input
  var $temp_employee_filter = $("#employee-filter");

  // 3.1 Empty the old filter's options
  $temp_employee_filter.empty(); // remove old options

  // start_loop_time = performance.now()
  // 3.2 Loop through the new unique options and append them as options to the select input

  for (var j = 0; j < newEmployeeOptionsUQ.length; j++) {
    $temp_employee_filter.append(
      $("<option></option>")
        .attr("value", newEmployeeOptionsUQ[j])
        .text(newEmployeeOptionsUQ[j])
    );
  }

  // end_time = performance.now()
  // console.log( 'newEmployeeOptionsUQ loop filter - benchmark:')
  // console.log(end_time - start_loop_time)

  // 3.3 Refresh/repaint the select picker so that the new options are visible.
  $("#employee-filter").selectpicker("refresh");

  // end_time = performance.now()
  // console.log( 'newEmployeeOptionsUQ filter - benchmark:')
  // console.log(end_time - start_time)

  //E. Update the Title filter options

  // start_time = performance.now()
  // 2. Filter to only the unique options

  let newTitleOptionsUQ = [...new Set(newTitleOptions)].sort();
  // 3. Update the select input
  var $temp_title_filter = $("#title-filter");

  // 3.1 Empty the old filter's options
  $temp_title_filter.empty();

  // 3.2 Loop through the new unique options and append them as options to the select input
  $.each(newTitleOptionsUQ, function (key, value) {
    $temp_title_filter.append(
      $("<option></option>").attr("value", value).text(value)
    );
  });

  // 3.3 Refresh/repaint the select picker so that the new options are visible.
  $("#title-filter").selectpicker("refresh");
}

function updateData() {
  // startChartSpinner()
  filter_is_applied = false;
  // console.log("UpdatedData started")

  // 1. Retrieve the raw data from the most recent query
  var data = window.mostRecentRawResult;
  // console.log("window.mostRecentRawResult");
  // console.log(data);

  // 2. Get the most recent selection for all four filters

  var recent_fiscal_years = fiscal_years_selected.fiscal_years;
  // console.log("recent_fiscal_years")
  // console.log(recent_fiscal_years)
  var recent_entities = entities_selected.entities;
  // console.log("recent_entities")
  // console.log(recent_entities)
  var recent_employees = employees_selected.employees;
  // console.log("recent_employees")
  // console.log(recent_employees)
  var recent_titles = titles_selected.titles;
  // console.log("recent_titles")
  // console.log(recent_titles)

  // 3. Filter the fiscal year if there is more than one filter selected. Otherwise do nothing to the data.
  if (recent_fiscal_years.length > 0) {
    var data_fy = data.filter((item) =>
      recent_fiscal_years.includes(item.fiscal_year)
    );
    filter_is_applied = true;
  } else {
    var data_fy = data;
  }
  // console.log("data_fy:");
  // console.log(data_fy);

  // 4. Filter the entity if there is more than one filter selected. Otherwise do nothing to the data.
  if (recent_entities.length > 0) {
    var data_entity = data_fy.filter((item) =>
      recent_entities.includes(item.entity_name)
    );
    filter_is_applied = true;
  } else {
    var data_entity = data_fy;
  }
  // console.log("data_entity:");
  // console.log(data_entity);

  // 5. Filter the employee if there is more than one filter selected. Otherwise do nothing to the data.
  if (recent_employees.length > 0) {
    var data_employee = data_entity.filter((item) =>
      recent_employees.includes(item.employee_name)
    );
    filter_is_applied = true;
    // console.log(data_employee);
  } else {
    var data_employee = data_entity;
  }
  // console.log("data_employee:");
  // console.log(data_employee);

  // 6. Filter the entity if there is more than one filter selected. Otherwise do nothing to the data.
  if (recent_titles.length > 0) {
    var data_title = data_employee.filter((item) =>
      recent_titles.includes(item.title)
    );
    filter_is_applied = true;
    // console.log(data_title);
  } else {
    var data_title = data_employee;
  }
  // console.log("data_title:");
  // console.log(data_title);

  // 10. Draw a new chart with our filtered data

  chartBarplot(data_title, "#emp-comp-chart");

  // .9 Update the table

  // Sort the data in descending order

  data_sorted = data_title.sort(fastSortTotal);

//   tabulator_table = new Tabulator("#tabulator-table", {
//     data: data_sorted,
//     pagination: "local",
//     paginationSize: 10,
//     paginationSizeSelector: [10, 25, 50, 100],
//     // responsiveLayout:"collapse",
//     height: 600,
//     layout: "fitDataTable",
//     columns: [
//       { title: "Id", field: "ids", titleDownload: "Id" },
//       {
//         title: "<i class='fas fa-calendar-alt'></i>&nbsp; Year",
//         field: "fiscal_year",
//         titleDownload: "Fiscal Year",
//       },
//       {
//         title: "<i class='fas fa-landmark'></i>&nbsp;Entity",
//         field: "entity_name",
//         titleDownload: "Entity",
//       },
//       {
//         title: "<i class='fas fa-user'></i>&nbsp;Employee</th>",
//         field: "employee_name",
//         titleDownload: "Employee",
//       },
//       {
//         title: "<i class='fas fa-briefcase'></i>&nbsp;Title",
//         field: "title",
//         titleDownload: "Title",
//       },
//       {
//         title: "<i class='fas fa-dollar-sign'></i>&nbsp;Wages",
//         field: "wages",
//         formatter: "money",
//         titleDownload: "Wages",
//         formatterParams: {
//           decimal: ".",
//           thousand: ",",
//           symbol: "$",
//           precision: 2,
//         },
//       },
//       {
//         title: "<i class='fas fa-dollar-sign'></i>&nbsp;Benefits",
//         field: "benefits",
//         formatter: "money",
//         titleDownload: "Benefits",
//         formatterParams: {
//           decimal: ".",
//           thousand: ",",
//           symbol: "$",
//           precision: 2,
//         },
//       },
//       {
//         title: "<i class='fas fa-dollar-sign'></i>&nbsp;Total",
//         field: "total",
//         formatter: "money",
//         titleDownload: "Total ",
//         formatterParams: {
//           decimal: ".",
//           thousand: ",",
//           symbol: "$",
//           precision: 2,
//         },
//       },
//     ],
//   });
}

// function chartBarplot(data_p, chart_id_p) {
//   $(chart_id_p).empty();
//   d3.select("svg").remove();

//   if (data_p != null) {
//     window.chartBarplotLastData = data_p;
//   } else {
//     data_p = window.chartBarplotLastData;
//   }

//   if (data_p.length < 1) {
//     $(chart_id_p).append(`<p class='text-danger'>
// 					Data must have at least 1 observations to plot a bar chart. 
// 					Refine your filters
// 				</p>`);
//     return;
//   }

//   var data_by_year = [];
//   data_p.reduce(function (res, value) {
//     // If there is an elements without a fiscal year, we want to populate it as empty.
//     if (!res[value.fiscal_year]) {
//       res[value.fiscal_year] = {
//         fiscal_year: value.fiscal_year,
//         wages: 0,
//         benefits: 0,
//       };
//       data_by_year.push(res[value.fiscal_year]);
//     }
//     res[value.fiscal_year].wages += value.wages;
//     res[value.fiscal_year].benefits += value.benefits;
//     return res;
//   }, {});

//   // console.log("data_by_year")
//   // console.log(data_by_year)

//   data = data_by_year;
//   // fix pre-processing
//   var keys = [];

//   for (key in data[0]) {
//     if (key != "fiscal_year") keys.push(key);
//   }

//   // console.log("keys:")
//   // console.log(keys)

//   data.forEach(function (d) {
//     d.total = 0;

//     keys.forEach(function (k) {
//       d.total += d[k];
//     });
//   });

//   data.sort(function (a, b) {
//     return a.fiscal_year - b.fiscal_year;
//   });

//   // var svg = d3.select("svg");
//   // var margin = { top: 30, right: 30, bottom: 75, left: 80 };

//   var container_width = $("#chart-container").width();

//   if (width > 400) {
//     var margin = { top: 0, right: 0, bottom: 75, left: 75 };
//     var height = (container_width * 2) / 3 - margin.top - margin.bottom;
//   } else {
//     var margin = { top: 0, right: 0, bottom: 50, left: 50 };
//     var height = container_width - margin.top - margin.bottom;
//   }

//   var width = container_width - margin.left - margin.right;

//   var width_no_margin = width + margin.left + margin.right;
//   var height_no_margin = height + margin.top + margin.bottom;

//   x_axis_title = "Fiscal Year";
//   y_axis_title = "Dollars($)";

//   var svg = d3
//     .select(chart_id_p)
//     .append("div")
//     .classed("svg-container", true) //container class to make it responsive
//     .append("svg")
//     .attr("preserveAspectRatio", "xMinYMin meet")
//     .attr("viewBox", `0 0 ${width_no_margin} ${height_no_margin}`)
//     //class to make it responsive
//     .classed("svg-content-responsive", true)
//     // .append("svg")
//     // .attr("width", width_no_margin)
//     // .attr("height", height_no_margin)
//     .append("g")
//     .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//   var x = d3.scaleBand().rangeRound([0, width]).paddingInner(0.05).align(0.1);

//   var y = d3.scaleLinear().rangeRound([height, 0]);

//   var z = d3.scaleOrdinal().range(["#3D4766", "#C85628"]);

//   x.domain(
//     data.map(function (d) {
//       return d.fiscal_year;
//     })
//   );

//   y.domain([
//     0,
//     d3.max(data, function (d) {
//       return d.total;
//     }),
//   ]).nice();

//   z.domain(keys);

//   // Add gridlines

//   // gridlines in x axis function
//   function make_x_gridlines() {
//     return d3.axisBottom(x).ticks(10);
//   }

//   // gridlines in y axis function
//   function make_y_gridlines() {
//     return d3.axisLeft(y).ticks(10);
//   }

//   // // add the X gridlines
//   svg
//     .append("g")
//     .attr("class", "grid")
//     .attr("transform", "translate(0," + height + ")")
//     .call(make_x_gridlines().tickSize(-height).tickFormat(""));

//   // add the Y gridlines
//   svg.append("g").attr("class", "grid").call(
//     make_y_gridlines().tickSize(-width)
//     // .tickFormat("")
//   );

//   // Add internal css so that they look pretty and can be downloaded. external css breaks the download chart functionality.
//   d3.selectAll(".tick").style("stroke", "lightgrey").style("opacity", "0.1");

//   d3.selectAll("path").style("stroke-width", "0");

//   stack_data = d3.stack().keys(keys)(data);

//   svg
//     .selectAll("rect")
//     .data(stack_data)
//     .enter()
//     .append("g")
//     .attr("fill", function (d) {
//       return z(d.key);
//     })
//     // .style("opacity", 0.8)
//     .selectAll("rect")
//     .data(function (d) {
//       return d;
//     })
//     .enter()
//     .append("rect")
//     .attr("x", function (d) {
//       return x(d.data.fiscal_year);
//     })
//     .attr("y", function (d) {
//       return y(d[1]);
//     })
//     .attr("height", function (d) {
//       return y(d[0]) - y(d[1]);
//     })
//     .attr("width", x.bandwidth());

//   // Add X-axis stuff
//   svg
//     .append("g")
//     .attr("class", "axis")
//     .attr("transform", "translate(0," + height + ")")
//     .call(d3.axisBottom(x));

//   svg
//     .append("text")
//     .attr(
//       "transform",
//       "translate(" + width / 2 + " ," + (height + margin.top + 20) + ")"
//     )
//     .style("text-anchor", "middle")
//     .text(x_axis_title);

//   // Add Y-axis stuff
//   svg.append("g").call(
//     d3.axisLeft(y).tickFormat(function (d) {
//       return formatNumberNatural(d);
//     })
//   );

//   // text label for the y axis
//   svg
//     .append("text")
//     .attr("transform", "rotate(-90)")
//     .attr("y", 0 - margin.left)
//     .attr("x", 0 - height / 2)
//     .attr("dy", "1em")
//     .style("text-anchor", "middle")
//     .text(y_axis_title);

//   var legend_rect_size = 20;
//   var legendHolder = svg
//     .append("g")
//     // translate the holder to the right side of the graph
//     .attr(
//       "transform",
//       "translate(" +
//         (-width + legend_rect_size) +
//         "," +
//         (-margin.top + legend_rect_size) +
//         ")"
//     )
//     .attr("class", "legendHolder");

//   var legend = legendHolder
//     .selectAll(".legend")
//     .data(keys.slice())
//     .enter()
//     .append("g")
//     .attr("class", "legend")
//     .attr("transform", function (d, i) {
//       return "translate(" + -50 * i + "," + 15 + ")";
//     })
//     .attr("width", 2 * legend_rect_size);

//   legend
//     .append("rect")
//     .attr("x", function (d, i) {
//       return width + 150 * i;
//     })
//     .attr("width", legend_rect_size)
//     .attr("height", legend_rect_size)
//     //.style("text-anchor", "end") //"startOffset"="100%
//     //.style("startOffset","100%") //"startOffset"="100%
//     .style("fill", z);

//   legend
//     .append("text")
//     //.attr("x", width - 24)
//     .attr("x", function (d, i) {
//       return width + 150 * i + legend_rect_size + 3;
//     })
//     .attr("y", 9)
//     .attr("dy", ".35em")
//     //.style("text-anchor", "end")
//     .text(function (d) {
//       return toTitleCase(d);
//     });

//   // init up the tooltip
//   var tooltip = d3
//     .select("body")
//     .append("div")
//     .attr("class", "svg-tooltip")
//     .style("position", "absolute")
//     .style("visibility", "hidden");

//   // create tooltip logic for mouse over
//   d3.selectAll("rect")
//     .on("mouseover", function (d) {
//       // change the selection style
//       d3.select(this).attr("stroke-width", "2").attr("stroke", "black");
//       // make the tooltip visible and update its text
//       tooltip
//         .style("visibility", "visible")
//         .text(formatNumberAlex(d[1] - d[0]));
//     })
//     .on("mousemove", function () {
//       tooltip
//         .style("top", d3.event.pageY - 10 + "px")
//         .style("left", d3.event.pageX + 10 + "px");
//     })
//     .on("mouseout", function () {
//       // change the selection style
//       d3.select(this).attr("stroke-width", "0");

//       tooltip.style("visibility", "hidden");
//     });
// }

function filterByFiscalYear() {
  // console.log("filterByFiscalYear started")
  // 1. Get the fiscal year options selected.
  var years = $("#fiscal-year-filter option:selected");

  //  2. make selections to an array format
  var selected = [];
  $(years).each(function (index, year) {
    selected.push([$(this).val()]);
  });

  // 3. flatten array
  selected = selected.flat();

  var selected_as_int = selected.map(function (x) {
    return parseInt(x, 10);
  });

  // 4. update the setter for the fiscal_years_selected listener.
  fiscal_years_selected.fiscal_years = selected_as_int;
}

function filterByEntity() {
  // console.log("filterByEntity started")
  // 1. Get the entity options selected.
  var entities = $("#entity-filter option:selected");

  //  2. make selections to an array format
  var selected = [];
  $(entities).each(function (index, entity) {
    selected.push([$(this).val()]);
  });

  // 3. flatten array
  selected = selected.flat();

  // 4 update the setter for the entities_selected listener.
  entities_selected.entities = selected;
}

function filterByEmployee() {
  // console.log("filterByEmployee started")
  // 1. Get the employee options selected.
  var employees = $("#employee-filter option:selected");

  //  2. make selections to an array format
  var selected = [];
  $(employees).each(function (index, employee) {
    selected.push([$(this).val()]);
  });

  // 3. flatten array
  selected = selected.flat();

  // 4 update the setter for the employees_selected listener.
  employees_selected.employees = selected;
}

function filterByTitle() {
  // console.log("filterByTitle started")
  // 1. Get the employee options selected.
  var titles = $("#title-filter option:selected");

  //  2. make selections to an array format
  var selected = [];
  $(titles).each(function (index, title) {
    selected.push([$(this).val()]);
  });

  // 3. flatten array
  selected = selected.flat();

  // 4. update the setter for the titles_selected listener.
  titles_selected.titles = selected;
}

// This function reads the query parameters from the URL and returns them as an object.
// It is used by `updateSubmitButton` to pre-fill the search input based on URL parameters.
function getUrlParams() {
  const params = {};
  window.location.search
    .substring(1)
    .split("&")
    .forEach((pair) => {
      const [key, value] = pair.split("=");
      params[decodeURIComponent(key)] = decodeURIComponent(value || "");
    });
  return params;
}


// This function checks the url bar and then puts the value into the search bar input and hits the submit button
// so that a user can use the search bar on the index.php page.
function updateSubmitButton() {
  var params = getUrlParams();

  var passed_name = params.name;
  // console.log('passed_name:' + passed_name)

  if (passed_name === undefined) {
  } else {
    document.getElementById("emp-search-input").value = passed_name;
    document.getElementById("emp-submit-button").click();
  }
}

window.onload = function () {
  updateSubmitButton();
};