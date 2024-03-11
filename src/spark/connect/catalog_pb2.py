# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/catalog.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from spark.connect import common_pb2 as spark_dot_connect_dot_common__pb2
from spark.connect import types_pb2 as spark_dot_connect_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bspark/connect/catalog.proto\x12\rspark.connect\x1a\x1aspark/connect/common.proto\x1a\x19spark/connect/types.proto\"\xc4\x0b\n\x07\x43\x61talog\x12:\n\x10\x63urrent_database\x18\x01 \x01(\x0b\x32\x1e.spark.connect.CurrentDatabaseH\x00\x12\x41\n\x14set_current_database\x18\x02 \x01(\x0b\x32!.spark.connect.SetCurrentDatabaseH\x00\x12\x36\n\x0elist_databases\x18\x03 \x01(\x0b\x32\x1c.spark.connect.ListDatabasesH\x00\x12\x30\n\x0blist_tables\x18\x04 \x01(\x0b\x32\x19.spark.connect.ListTablesH\x00\x12\x36\n\x0elist_functions\x18\x05 \x01(\x0b\x32\x1c.spark.connect.ListFunctionsH\x00\x12\x32\n\x0clist_columns\x18\x06 \x01(\x0b\x32\x1a.spark.connect.ListColumnsH\x00\x12\x32\n\x0cget_database\x18\x07 \x01(\x0b\x32\x1a.spark.connect.GetDatabaseH\x00\x12,\n\tget_table\x18\x08 \x01(\x0b\x32\x17.spark.connect.GetTableH\x00\x12\x32\n\x0cget_function\x18\t \x01(\x0b\x32\x1a.spark.connect.GetFunctionH\x00\x12\x38\n\x0f\x64\x61tabase_exists\x18\n \x01(\x0b\x32\x1d.spark.connect.DatabaseExistsH\x00\x12\x32\n\x0ctable_exists\x18\x0b \x01(\x0b\x32\x1a.spark.connect.TableExistsH\x00\x12\x38\n\x0f\x66unction_exists\x18\x0c \x01(\x0b\x32\x1d.spark.connect.FunctionExistsH\x00\x12\x43\n\x15\x63reate_external_table\x18\r \x01(\x0b\x32\".spark.connect.CreateExternalTableH\x00\x12\x32\n\x0c\x63reate_table\x18\x0e \x01(\x0b\x32\x1a.spark.connect.CreateTableH\x00\x12\x35\n\x0e\x64rop_temp_view\x18\x0f \x01(\x0b\x32\x1b.spark.connect.DropTempViewH\x00\x12\x42\n\x15\x64rop_global_temp_view\x18\x10 \x01(\x0b\x32!.spark.connect.DropGlobalTempViewH\x00\x12>\n\x12recover_partitions\x18\x11 \x01(\x0b\x32 .spark.connect.RecoverPartitionsH\x00\x12,\n\tis_cached\x18\x12 \x01(\x0b\x32\x17.spark.connect.IsCachedH\x00\x12\x30\n\x0b\x63\x61\x63he_table\x18\x13 \x01(\x0b\x32\x19.spark.connect.CacheTableH\x00\x12\x34\n\runcache_table\x18\x14 \x01(\x0b\x32\x1b.spark.connect.UncacheTableH\x00\x12\x30\n\x0b\x63lear_cache\x18\x15 \x01(\x0b\x32\x19.spark.connect.ClearCacheH\x00\x12\x34\n\rrefresh_table\x18\x16 \x01(\x0b\x32\x1b.spark.connect.RefreshTableH\x00\x12\x37\n\x0frefresh_by_path\x18\x17 \x01(\x0b\x32\x1c.spark.connect.RefreshByPathH\x00\x12\x38\n\x0f\x63urrent_catalog\x18\x18 \x01(\x0b\x32\x1d.spark.connect.CurrentCatalogH\x00\x12?\n\x13set_current_catalog\x18\x19 \x01(\x0b\x32 .spark.connect.SetCurrentCatalogH\x00\x12\x34\n\rlist_catalogs\x18\x1a \x01(\x0b\x32\x1b.spark.connect.ListCatalogsH\x00\x42\n\n\x08\x63\x61t_type\"\x11\n\x0f\x43urrentDatabase\"%\n\x12SetCurrentDatabase\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\"1\n\rListDatabases\x12\x14\n\x07pattern\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_pattern\"P\n\nListTables\x12\x14\n\x07\x64\x62_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07pattern\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\n\n\x08_db_nameB\n\n\x08_pattern\"S\n\rListFunctions\x12\x14\n\x07\x64\x62_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07pattern\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\n\n\x08_db_nameB\n\n\x08_pattern\"C\n\x0bListColumns\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x07\x64\x62_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_db_name\"\x1e\n\x0bGetDatabase\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\"@\n\x08GetTable\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x07\x64\x62_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_db_name\"F\n\x0bGetFunction\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x14\n\x07\x64\x62_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_db_name\"!\n\x0e\x44\x61tabaseExists\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\"C\n\x0bTableExists\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x14\n\x07\x64\x62_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_db_name\"I\n\x0e\x46unctionExists\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x14\n\x07\x64\x62_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_db_name\"\x90\x02\n\x13\x43reateExternalTable\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x11\n\x04path\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06source\x18\x03 \x01(\tH\x01\x88\x01\x01\x12,\n\x06schema\x18\x04 \x01(\x0b\x32\x17.spark.connect.DataTypeH\x02\x88\x01\x01\x12@\n\x07options\x18\x05 \x03(\x0b\x32/.spark.connect.CreateExternalTable.OptionsEntry\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x07\n\x05_pathB\t\n\x07_sourceB\t\n\x07_schema\"\xaa\x02\n\x0b\x43reateTable\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x11\n\x04path\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06source\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x04 \x01(\tH\x02\x88\x01\x01\x12,\n\x06schema\x18\x05 \x01(\x0b\x32\x17.spark.connect.DataTypeH\x03\x88\x01\x01\x12\x38\n\x07options\x18\x06 \x03(\x0b\x32\'.spark.connect.CreateTable.OptionsEntry\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x07\n\x05_pathB\t\n\x07_sourceB\x0e\n\x0c_descriptionB\t\n\x07_schema\"!\n\x0c\x44ropTempView\x12\x11\n\tview_name\x18\x01 \x01(\t\"\'\n\x12\x44ropGlobalTempView\x12\x11\n\tview_name\x18\x01 \x01(\t\"\'\n\x11RecoverPartitions\x12\x12\n\ntable_name\x18\x01 \x01(\t\"\x1e\n\x08IsCached\x12\x12\n\ntable_name\x18\x01 \x01(\t\"k\n\nCacheTable\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x37\n\rstorage_level\x18\x02 \x01(\x0b\x32\x1b.spark.connect.StorageLevelH\x00\x88\x01\x01\x42\x10\n\x0e_storage_level\"\"\n\x0cUncacheTable\x12\x12\n\ntable_name\x18\x01 \x01(\t\"\x0c\n\nClearCache\"\"\n\x0cRefreshTable\x12\x12\n\ntable_name\x18\x01 \x01(\t\"\x1d\n\rRefreshByPath\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x10\n\x0e\x43urrentCatalog\")\n\x11SetCurrentCatalog\x12\x14\n\x0c\x63\x61talog_name\x18\x01 \x01(\t\"0\n\x0cListCatalogs\x12\x14\n\x07pattern\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_patternB6\n\x1eorg.apache.spark.connect.protoP\x01Z\x12internal/generatedb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spark.connect.catalog_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036org.apache.spark.connect.protoP\001Z\022internal/generated'
  _globals['_CREATEEXTERNALTABLE_OPTIONSENTRY']._options = None
  _globals['_CREATEEXTERNALTABLE_OPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_CREATETABLE_OPTIONSENTRY']._options = None
  _globals['_CREATETABLE_OPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_CATALOG']._serialized_start=102
  _globals['_CATALOG']._serialized_end=1578
  _globals['_CURRENTDATABASE']._serialized_start=1580
  _globals['_CURRENTDATABASE']._serialized_end=1597
  _globals['_SETCURRENTDATABASE']._serialized_start=1599
  _globals['_SETCURRENTDATABASE']._serialized_end=1636
  _globals['_LISTDATABASES']._serialized_start=1638
  _globals['_LISTDATABASES']._serialized_end=1687
  _globals['_LISTTABLES']._serialized_start=1689
  _globals['_LISTTABLES']._serialized_end=1769
  _globals['_LISTFUNCTIONS']._serialized_start=1771
  _globals['_LISTFUNCTIONS']._serialized_end=1854
  _globals['_LISTCOLUMNS']._serialized_start=1856
  _globals['_LISTCOLUMNS']._serialized_end=1923
  _globals['_GETDATABASE']._serialized_start=1925
  _globals['_GETDATABASE']._serialized_end=1955
  _globals['_GETTABLE']._serialized_start=1957
  _globals['_GETTABLE']._serialized_end=2021
  _globals['_GETFUNCTION']._serialized_start=2023
  _globals['_GETFUNCTION']._serialized_end=2093
  _globals['_DATABASEEXISTS']._serialized_start=2095
  _globals['_DATABASEEXISTS']._serialized_end=2128
  _globals['_TABLEEXISTS']._serialized_start=2130
  _globals['_TABLEEXISTS']._serialized_end=2197
  _globals['_FUNCTIONEXISTS']._serialized_start=2199
  _globals['_FUNCTIONEXISTS']._serialized_end=2272
  _globals['_CREATEEXTERNALTABLE']._serialized_start=2275
  _globals['_CREATEEXTERNALTABLE']._serialized_end=2547
  _globals['_CREATEEXTERNALTABLE_OPTIONSENTRY']._serialized_start=2470
  _globals['_CREATEEXTERNALTABLE_OPTIONSENTRY']._serialized_end=2516
  _globals['_CREATETABLE']._serialized_start=2550
  _globals['_CREATETABLE']._serialized_end=2848
  _globals['_CREATETABLE_OPTIONSENTRY']._serialized_start=2470
  _globals['_CREATETABLE_OPTIONSENTRY']._serialized_end=2516
  _globals['_DROPTEMPVIEW']._serialized_start=2850
  _globals['_DROPTEMPVIEW']._serialized_end=2883
  _globals['_DROPGLOBALTEMPVIEW']._serialized_start=2885
  _globals['_DROPGLOBALTEMPVIEW']._serialized_end=2924
  _globals['_RECOVERPARTITIONS']._serialized_start=2926
  _globals['_RECOVERPARTITIONS']._serialized_end=2965
  _globals['_ISCACHED']._serialized_start=2967
  _globals['_ISCACHED']._serialized_end=2997
  _globals['_CACHETABLE']._serialized_start=2999
  _globals['_CACHETABLE']._serialized_end=3106
  _globals['_UNCACHETABLE']._serialized_start=3108
  _globals['_UNCACHETABLE']._serialized_end=3142
  _globals['_CLEARCACHE']._serialized_start=3144
  _globals['_CLEARCACHE']._serialized_end=3156
  _globals['_REFRESHTABLE']._serialized_start=3158
  _globals['_REFRESHTABLE']._serialized_end=3192
  _globals['_REFRESHBYPATH']._serialized_start=3194
  _globals['_REFRESHBYPATH']._serialized_end=3223
  _globals['_CURRENTCATALOG']._serialized_start=3225
  _globals['_CURRENTCATALOG']._serialized_end=3241
  _globals['_SETCURRENTCATALOG']._serialized_start=3243
  _globals['_SETCURRENTCATALOG']._serialized_end=3284
  _globals['_LISTCATALOGS']._serialized_start=3286
  _globals['_LISTCATALOGS']._serialized_end=3334
# @@protoc_insertion_point(module_scope)
