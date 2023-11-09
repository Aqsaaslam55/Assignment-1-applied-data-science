import pandas as pd
import matplotlib.pyplot as plt
file_name = 'Fuel Consumption.csv'
pd.set_option('display.max_columns', None)
df= pd.read_csv(file_name, encoding='latin1')
print(df)



def fuel_consumption(df):
    selected_makes = ['Audi', 'BMW', 'Bentley']
    filtered_data = df[df['MAKE'].isin(selected_makes)]
    fuel_consumption_data = filtered_data.groupby(['YEAR', 'MAKE'])['FUEL CONSUMPTION'].mean().unstack()

    # Create a line chart
    plt.figure(figsize=(10, 6))
    for make in selected_makes:
        plt.plot(fuel_consumption_data.index, fuel_consumption_data[make], label=make)

    plt.xlabel('Year (Model Year)')
    plt.ylabel('Fuel Consumption (L/100 km)')
    plt.title('Fuel Consumption Comparison for Audi, BMW, and Bentley')
    plt.legend()
    plt.grid(True)
    plt.show()


fuel_consumption(df)




def consumption_by_fuel_type(df):

    fuel_consumption_data = df.groupby('FUEL')['FUEL CONSUMPTION'].mean()
    plt.figure(figsize=(10, 6))
    fuel_consumption_data.plot(kind='bar', color='skyblue')
    plt.xlabel('Fuel Type')
    plt.ylabel('Mean Fuel Consumption (L/100 km)')
    plt.title('Fuel Consumption by Fuel Type')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the chart or save it as an image
    plt.show()

consumption_by_fuel_type(df)



def plot_vehicle_class_pie_chart(df):
    grouped_data = df.groupby('VEHICLE CLASS')['HWY (L/100 km)'].mean()
    top_10_classes = grouped_data.nlargest(10)
    plt.figure(figsize=(8, 8))
    plt.pie(top_10_classes, labels=top_10_classes.index, autopct='%1.1f%%', startangle=140)
    plt.title('Top 10 Vehicle Classes by Highway Fuel Consumption (L/100 km)')
    plt.show()
    plt.show()
plot_vehicle_class_pie_chart(df)

















