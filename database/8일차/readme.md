## QuerySet API

* gt

```python
Entry.objects.filter(id__gt=4)
```

```sql
SELECT ... WHERE id > 4;
```

* gte

```python
Entry.objects.filter(id__gte=4)
```

```sql
SELECT ... WHERE id >= 4;
```

* lt, lte

```python
Entry.objects.filter(id__lt=4)
Entry.objects.filter(id__lte=4)
```

```sql
SELECT ... WHERE id < 4;
SELECT ... WHERE id <= 4;
```

* in

```python
Entry.objects.filter(id__in=[1, 3, 4])
Entry.objects.filter(headline__in='abc')
```

```sql
SELECT ... WHERE id IN (1, 3, 4);
SELECT ... WHERE headline IN ('a', 'b', 'c');
```

* startswith

```python
Entry.objects.filter(headline__startswith='Lennon')
```

```sql
SELECT ... WHERE headline LIKE 'Lennon%';
```

* istartswith

```python
Entry.objects.filter(headline__istartswith='Lennon')
```

```sql
SELECT ... WHERE headline ILIKE 'Lennon%';
```

