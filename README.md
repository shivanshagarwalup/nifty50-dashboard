# Nifty 50

*Generated with ForgeUI on 3/18/2026*

## Original Prompt
> Develop a modern, high-usability dashboard for Nifty 50 historical performance over the past 20 years.

**User Experience & Interaction Details:**

1.  **Dashboard Entry**: Upon loading, the entire dashboard content should smoothly fade in, providing an elegant and welcoming visual feedback.
2.  **Primary Actions (Clear CTAs)**:
    *   **Date Range Selector**: A prominent, neomorphic date range selector (e.g., soft-shadowed buttons or dropdowns) should be easily accessible. It must allow users to select predefined periods within the 20-year dataset (e.g., "Last 1 Year", "Last 5 Years", "Last 10 Years", "All 20 Years") or specify a custom start and end date. This selector is a primary control for the data displayed.
    *   **Data Granularity**: Implement clear, discernible neomorphic radio buttons or a dropdown for users to switch between "Daily", "Weekly", and "Monthly" data aggregation for the Nifty 50 performance.
    *   **Export Data**: A distinct, soft-shadowed button should be available to allow users to download the currently displayed historical Nifty data as a CSV or similar format.
3.  **Graph Interaction**: The main Nifty 50 line chart must be highly interactive.
    *   **Hover Tooltip**: On mouse hover over the chart, a clear, high-contrast tooltip should display the exact Nifty value and corresponding date for that data point.
    *   **Zoom & Pan**: Users should be able to intuitively zoom into specific timeframes on the graph and pan across the historical data for detailed inspection.
4.  **Feedback**: All interactive elements (buttons, selectors, date pickers) must provide smooth, discernible visual feedback on hover, focus, and active states, consistent with the neomorphic aesthetic.

**Visual Design & Aesthetics:**

1.  **Aesthetic**: Apply a consistent Soft UI / Neomorphism aesthetic throughout the dashboard. This includes:
    *   **Soft Shadows**: Utilize subtle, diffused shadows (inner and outer) to give UI elements (cards, buttons, input fields, graph container) a perceived physical depth, making them appear "pushed in" or "raised out" from the background.
    *   **Rounded Corners**: All UI components, including cards, buttons, and input fields, should feature gently rounded corners.
    *   **Physical Feel**: The overall design should evoke a tactile, physical sensation for interactive elements.
2.  **Spacing**: Ensure generous and comfortable spacing between all UI elements, component sections, and within components themselves. All spacing values should be defined using `rem` units for consistency and accessibility.
3.  **Accessibility**:
    *   **High Contrast**: Maintain high contrast ratios for all text against backgrounds and for interactive elements to ensure excellent readability and discernment for all users (WCAG AA or AAA where possible).
    *   **Discernible Elements**: Interactive elements must be clearly distinguishable from static content, even without relying solely on color (e.g., via their neomorphic design, soft shadows, and hover effects).

**Technical Implementation Details:**

1.  **Framework Combination**: Use HTML for the semantic structure. Style the dashboard primarily with **Tailwind CSS** to achieve the neomorphic aesthetic, spacing, and responsive layout. Intelligently integrate **Bootstrap** for foundational components or grid structures where beneficial, ensuring its default styling is overridden by or harmonized with the Tailwind-driven neomorphic design.
2.  **Layout**: Implement a **dense but readable grid layout** for the entire dashboard.
    *   **Main Graph Area**: The interactive Nifty 50 line graph should occupy the most prominent and largest section, typically at the top or center-top.
    *   **Key Metrics Cards**: Below the main graph, arrange a set of supplementary "Key Metrics" cards in a responsive grid. These cards must have **uniform heights** where possible. Each card should display an important Nifty 50 performance indicator (e.g., "Current Value", "20-Year CAGR", "52-Week High", "52-Week Low", "Year-to-Date Change"). These metric cards must dynamically update their displayed values based on the user's selected date range and granularity.
3.  **Data Visibility**: Emphasize displaying data clearly and legibly. Text within charts and cards should be appropriately sized and contrasted.
4.  **Data Source**: The dashboard should be populated with a placeholder or simulated dataset representing historical Nifty 50 closing prices over the last 20 years. This dataset should support daily, weekly, and monthly aggregation.
5.  **Graphing Library**: Integrate an interactive JavaScript charting library (e.g., Chart.js, ApexCharts, Echarts) capable of rendering line charts, handling large datasets efficiently, and providing the specified interactive features like hover tooltips, zoom, and pan capabilities.


## HTML + CSS Usage

1. **Open File**: Open `index.html` in your browser.
2. **Integration**: Copy the HTML structure and CSS styles into your own project files.
        

## Structure
The ZIP file contains the raw source code for the component.
- **meta.json**: Generation metadata.

---
*Powered by ForgeUI*
