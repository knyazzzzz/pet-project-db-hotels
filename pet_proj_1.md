### Пет-проект на тему *Данные о бронировании отелей*

```
Импорт библиотеки pandas
```


```python
import pandas as pd
```

```
Загрузка .csv файла с кодировкой windows-1251 и разделителем ';'
```


```python
bk = pd.read_csv('https://stepik.org/media/attachments/lesson/360344/bookings.csv', 
                     encoding = 'windows-1251', 
                     sep = ';')
```


```python
bookings_head = bk[:7]
```

```
Проверка размеров таблицы и типов переменных в ней
```


```python
bk.shape
```




    (119390, 21)




```python
bk.dtypes
```




    Hotel                         object
    Is Canceled                    int64
    Lead Time                      int64
    arrival full date             object
    Arrival Date Year              int64
    Arrival Date Month            object
    Arrival Date Week Number       int64
    Arrival Date Day of Month      int64
    Stays in Weekend nights        int64
    Stays in week nights           int64
    stays total nights             int64
    Adults                         int64
    Children                     float64
    Babies                         int64
    Meal                          object
    Country                       object
    Reserved Room Type            object
    Assigned room type            object
    customer type                 object
    Reservation Status            object
    Reservation status_date       object
    dtype: object



```
Стандартизируем названия колонок
```


```python
bk = bk.rename(columns = {'Hotel' : 'hotel', 
                     'Is Canceled' : 'is_cancelled', 
                     'Lead Time' : 'lead_time', 
                     'arrival full date' : 'arrival_full_date',
                     'Arrival Date Year' : 'arrival_date_year', 
                     'Arrival Date Month' : 'arrival_date_month', 
                     'Arrival Date Week Number' : 'arrival_date_week_number',
                     'Arrival Date Day of Month' : 'arrival_date_day_of_month', 
                     'Stays in Weekend nights' : 'stays_in_weekend_nights',
                     'Stays in week nights' : 'stays_in_week_nights', 
                     'stays total nights' : 'stays_total_nights',
                     'Adults' : 'adults', 
                     'Children' : 'children',
                     'Babies' : 'babies', 
                     'Meal' : 'meal', 
                     'Country' : 'country', 
                     'Reserved Room Type' : 'reserved_room_type', 
                     'Assigned room type' : 'assigned_room_type',
                     'customer type' : 'customer_type', 
                     'Reservation Status' : 'reservation_status', 
                     'Reservation status_date' : 'reservation_status_date'})
```


>Топ-5 стран, из которых пользователи совершили наибольшее число бронирований



```python
bk.query('is_cancelled == 0')\
    .groupby('country', as_index = False)\
    .agg({'is_cancelled':'count'})\
    .sort_values('is_cancelled', ascending = False)[:5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>is_cancelled</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>125</th>
      <td>PRT</td>
      <td>21071</td>
    </tr>
    <tr>
      <th>57</th>
      <td>GBR</td>
      <td>9676</td>
    </tr>
    <tr>
      <th>54</th>
      <td>FRA</td>
      <td>8481</td>
    </tr>
    <tr>
      <th>50</th>
      <td>ESP</td>
      <td>6391</td>
    </tr>
    <tr>
      <th>42</th>
      <td>DEU</td>
      <td>6069</td>
    </tr>
  </tbody>
</table>
</div>




>На сколько ночей в среднем бронируют отели разных типов



```python
round(bk.groupby('hotel', as_index = False)\
    .agg({'stays_total_nights':'mean'}),2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>hotel</th>
      <th>stays_total_nights</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>City Hotel</td>
      <td>2.98</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Resort Hotel</td>
      <td>4.32</td>
    </tr>
  </tbody>
</table>
</div>



>Сколько раз фактический номер отличался от забронированного


```python
bk.query('assigned_room_type != reserved_room_type')\
    .agg({'assigned_room_type':'count'})
```




    assigned_room_type    14917
    dtype: int64



>Самые популярные месяцы для брони в 2016 и 2017


```python
bk.query('arrival_date_year == 2016')\
    .groupby('arrival_date_month', as_index = False)\
    .agg({'country':'count'})\
    .sort_values('country', ascending = False)[:1]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>arrival_date_month</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>October</td>
      <td>6176</td>
    </tr>
  </tbody>
</table>
</div>




```python
bk.query('arrival_date_year == 2017')\
    .groupby('arrival_date_month', as_index = False)\
    .agg({'country':'count'})\
    .sort_values('country', ascending = False)[:1]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>arrival_date_month</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>May</td>
      <td>6313</td>
    </tr>
  </tbody>
</table>
</div>



> В какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждом году.


```python
bk.query('hotel == "City Hotel" & is_cancelled == 1')\
    .groupby(['arrival_date_year','arrival_date_month'], as_index = False)\
    .agg({'is_cancelled':'count'})\
    .sort_values(['arrival_date_year','is_cancelled'], ascending = False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>arrival_date_year</th>
      <th>arrival_date_month</th>
      <th>is_cancelled</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>25</th>
      <td>2017</td>
      <td>May</td>
      <td>2217</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2017</td>
      <td>April</td>
      <td>1926</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2017</td>
      <td>June</td>
      <td>1808</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2017</td>
      <td>July</td>
      <td>1324</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2017</td>
      <td>March</td>
      <td>1278</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2017</td>
      <td>August</td>
      <td>1123</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2017</td>
      <td>January</td>
      <td>1044</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2017</td>
      <td>February</td>
      <td>971</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>October</td>
      <td>1947</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>June</td>
      <td>1720</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>September</td>
      <td>1567</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>April</td>
      <td>1539</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>May</td>
      <td>1436</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>November</td>
      <td>1360</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>August</td>
      <td>1247</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>March</td>
      <td>1108</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>December</td>
      <td>1072</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>July</td>
      <td>1043</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>February</td>
      <td>930</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>January</td>
      <td>438</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2015</td>
      <td>September</td>
      <td>1543</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>October</td>
      <td>1321</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>August</td>
      <td>1232</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>July</td>
      <td>939</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>December</td>
      <td>668</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>November</td>
      <td>301</td>
    </tr>
  </tbody>
</table>
</div>



> Какая из числовых характеристик adults, children и babies имеет наибольшее среднее значение


```python
bk.describe()[1:2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>is_cancelled</th>
      <th>lead_time</th>
      <th>arrival_date_year</th>
      <th>arrival_date_week_number</th>
      <th>arrival_date_day_of_month</th>
      <th>stays_in_weekend_nights</th>
      <th>stays_in_week_nights</th>
      <th>stays_total_nights</th>
      <th>adults</th>
      <th>children</th>
      <th>babies</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>mean</th>
      <td>0.370416</td>
      <td>104.011416</td>
      <td>2016.156554</td>
      <td>27.165173</td>
      <td>15.798241</td>
      <td>0.927599</td>
      <td>2.500302</td>
      <td>3.4279</td>
      <td>1.856403</td>
      <td>0.10389</td>
      <td>0.007949</td>
    </tr>
  </tbody>
</table>
</div>



> Создадим колонку total_kids, объединив children и babies. Отели какого типа в среднем пользуются большей популярностью у клиентов с детьми? 


```python
bk['total_kids'] = bk.children + bk.babies
```


```python
round(bk.groupby('hotel', as_index = False)\
    .agg({'total_kids' : 'mean'})\
    .sort_values('total_kids', ascending = False),2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>hotel</th>
      <th>total_kids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Resort Hotel</td>
      <td>0.14</td>
    </tr>
    <tr>
      <th>0</th>
      <td>City Hotel</td>
      <td>0.10</td>
    </tr>
  </tbody>
</table>
</div>



> Создадим переменную has_kids, которая принимает значение True, если клиент при бронировании указал хотя бы одного ребенка (total_kids), и False – в противном случае. Посчитаем отношение количества ушедших пользователей к общему количеству клиентов, выраженное в процентах (churn rate). Укажите, среди какой группы показатель выше.


```python
bk['has_kids'] = bk['total_kids'] > 0
```


```python
bk.query('has_kids == True and is_cancelled == 1').agg({'hotel'  : 'count'}) / bk.query('has_kids == True').agg({'hotel'  : 'count'})
```




    hotel    0.349228
    dtype: float64




```python
bk.query('has_kids == False and is_cancelled == 1').agg({'hotel'  : 'count'}) / bk.query('has_kids == False').agg({'hotel'  : 'count'})
```




    hotel    0.372213
    dtype: float64




```python

```
