#!/usr/bin/env python
# coding: utf-8

# ### Пет-проект на тему *Данные о бронировании отелей*
# 
# ```
# Импорт библиотеки pandas
# ```

# In[118]:


import pandas as pd


# ```
# Загрузка .csv файла с кодировкой windows-1251 и разделителем ';'
# ```

# In[119]:


bk = pd.read_csv('https://stepik.org/media/attachments/lesson/360344/bookings.csv', 
                     encoding = 'windows-1251', 
                     sep = ';')


# In[120]:


bookings_head = bk[:7]


# ```
# Проверка размеров таблицы и типов переменных в ней
# ```

# In[121]:


bk.shape


# In[122]:


bk.dtypes


# ```
# Стандартизируем названия колонок
# ```

# In[123]:


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


# 
# >Топ-5 стран, из которых пользователи совершили наибольшее число бронирований
# 

# In[126]:


bk.query('is_cancelled == 0')    .groupby('country', as_index = False)    .agg({'is_cancelled':'count'})    .sort_values('is_cancelled', ascending = False)[:5]


# 
# >На сколько ночей в среднем бронируют отели разных типов
# 

# In[127]:


round(bk.groupby('hotel', as_index = False)    .agg({'stays_total_nights':'mean'}),2)


# >Сколько раз фактический номер отличался от забронированного

# In[68]:


bk.query('assigned_room_type != reserved_room_type')    .agg({'assigned_room_type':'count'})


# >Самые популярные месяцы для брони в 2016 и 2017

# In[136]:


bk.query('arrival_date_year == 2016')    .groupby('arrival_date_month', as_index = False)    .agg({'country':'count'})    .sort_values('country', ascending = False)[:1]


# In[137]:


bk.query('arrival_date_year == 2017')    .groupby('arrival_date_month', as_index = False)    .agg({'country':'count'})    .sort_values('country', ascending = False)[:1]


# > В какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждом году.

# In[79]:


bk.query('hotel == "City Hotel" & is_cancelled == 1')    .groupby(['arrival_date_year','arrival_date_month'], as_index = False)    .agg({'is_cancelled':'count'})    .sort_values(['arrival_date_year','is_cancelled'], ascending = False)


# > Какая из числовых характеристик adults, children и babies имеет наибольшее среднее значение

# In[90]:


bk.describe()[1:2]


# > Создадим колонку total_kids, объединив children и babies. Отели какого типа в среднем пользуются большей популярностью у клиентов с детьми? 

# In[139]:


bk['total_kids'] = bk.children + bk.babies


# In[141]:


round(bk.groupby('hotel', as_index = False)    .agg({'total_kids' : 'mean'})    .sort_values('total_kids', ascending = False),2)


# > Создадим переменную has_kids, которая принимает значение True, если клиент при бронировании указал хотя бы одного ребенка (total_kids), и False – в противном случае. Посчитаем отношение количества ушедших пользователей к общему количеству клиентов, выраженное в процентах (churn rate). Укажите, среди какой группы показатель выше.

# In[142]:


bk['has_kids'] = bk['total_kids'] > 0


# In[145]:


bk.query('has_kids == True and is_cancelled == 1').agg({'hotel'  : 'count'}) / bk.query('has_kids == True').agg({'hotel'  : 'count'})


# In[146]:


bk.query('has_kids == False and is_cancelled == 1').agg({'hotel'  : 'count'}) / bk.query('has_kids == False').agg({'hotel'  : 'count'})


# In[ ]:




