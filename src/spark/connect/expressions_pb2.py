# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/expressions.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from spark.connect import types_pb2 as spark_dot_connect_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fspark/connect/expressions.proto\x12\rspark.connect\x1a\x19google/protobuf/any.proto\x1a\x19spark/connect/types.proto\"\xe2#\n\nExpression\x12\x34\n\x07literal\x18\x01 \x01(\x0b\x32!.spark.connect.Expression.LiteralH\x00\x12M\n\x14unresolved_attribute\x18\x02 \x01(\x0b\x32-.spark.connect.Expression.UnresolvedAttributeH\x00\x12K\n\x13unresolved_function\x18\x03 \x01(\x0b\x32,.spark.connect.Expression.UnresolvedFunctionH\x00\x12G\n\x11\x65xpression_string\x18\x04 \x01(\x0b\x32*.spark.connect.Expression.ExpressionStringH\x00\x12\x43\n\x0funresolved_star\x18\x05 \x01(\x0b\x32(.spark.connect.Expression.UnresolvedStarH\x00\x12\x30\n\x05\x61lias\x18\x06 \x01(\x0b\x32\x1f.spark.connect.Expression.AliasH\x00\x12.\n\x04\x63\x61st\x18\x07 \x01(\x0b\x32\x1e.spark.connect.Expression.CastH\x00\x12\x45\n\x10unresolved_regex\x18\x08 \x01(\x0b\x32).spark.connect.Expression.UnresolvedRegexH\x00\x12\x39\n\nsort_order\x18\t \x01(\x0b\x32#.spark.connect.Expression.SortOrderH\x00\x12\x43\n\x0flambda_function\x18\n \x01(\x0b\x32(.spark.connect.Expression.LambdaFunctionH\x00\x12\x32\n\x06window\x18\x0b \x01(\x0b\x32 .spark.connect.Expression.WindowH\x00\x12T\n\x18unresolved_extract_value\x18\x0c \x01(\x0b\x32\x30.spark.connect.Expression.UnresolvedExtractValueH\x00\x12?\n\rupdate_fields\x18\r \x01(\x0b\x32&.spark.connect.Expression.UpdateFieldsH\x00\x12\x63\n unresolved_named_lambda_variable\x18\x0e \x01(\x0b\x32\x37.spark.connect.Expression.UnresolvedNamedLambdaVariableH\x00\x12]\n#common_inline_user_defined_function\x18\x0f \x01(\x0b\x32..spark.connect.CommonInlineUserDefinedFunctionH\x00\x12\x34\n\rcall_function\x18\x10 \x01(\x0b\x32\x1b.spark.connect.CallFunctionH\x00\x12*\n\textension\x18\xe7\x07 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x1a\xa2\x05\n\x06Window\x12\x32\n\x0fwindow_function\x18\x01 \x01(\x0b\x32\x19.spark.connect.Expression\x12\x31\n\x0epartition_spec\x18\x02 \x03(\x0b\x32\x19.spark.connect.Expression\x12\x37\n\norder_spec\x18\x03 \x03(\x0b\x32#.spark.connect.Expression.SortOrder\x12@\n\nframe_spec\x18\x04 \x01(\x0b\x32,.spark.connect.Expression.Window.WindowFrame\x1a\xb5\x03\n\x0bWindowFrame\x12J\n\nframe_type\x18\x01 \x01(\x0e\x32\x36.spark.connect.Expression.Window.WindowFrame.FrameType\x12I\n\x05lower\x18\x02 \x01(\x0b\x32:.spark.connect.Expression.Window.WindowFrame.FrameBoundary\x12I\n\x05upper\x18\x03 \x01(\x0b\x32:.spark.connect.Expression.Window.WindowFrame.FrameBoundary\x1as\n\rFrameBoundary\x12\x15\n\x0b\x63urrent_row\x18\x01 \x01(\x08H\x00\x12\x13\n\tunbounded\x18\x02 \x01(\x08H\x00\x12*\n\x05value\x18\x03 \x01(\x0b\x32\x19.spark.connect.ExpressionH\x00\x42\n\n\x08\x62oundary\"O\n\tFrameType\x12\x18\n\x14\x46RAME_TYPE_UNDEFINED\x10\x00\x12\x12\n\x0e\x46RAME_TYPE_ROW\x10\x01\x12\x14\n\x10\x46RAME_TYPE_RANGE\x10\x02\x1a\x89\x03\n\tSortOrder\x12(\n\x05\x63hild\x18\x01 \x01(\x0b\x32\x19.spark.connect.Expression\x12\x44\n\tdirection\x18\x02 \x01(\x0e\x32\x31.spark.connect.Expression.SortOrder.SortDirection\x12G\n\rnull_ordering\x18\x03 \x01(\x0e\x32\x30.spark.connect.Expression.SortOrder.NullOrdering\"l\n\rSortDirection\x12\x1e\n\x1aSORT_DIRECTION_UNSPECIFIED\x10\x00\x12\x1c\n\x18SORT_DIRECTION_ASCENDING\x10\x01\x12\x1d\n\x19SORT_DIRECTION_DESCENDING\x10\x02\"U\n\x0cNullOrdering\x12\x1a\n\x16SORT_NULLS_UNSPECIFIED\x10\x00\x12\x14\n\x10SORT_NULLS_FIRST\x10\x01\x12\x13\n\x0fSORT_NULLS_LAST\x10\x02\x1a|\n\x04\x43\x61st\x12\'\n\x04\x65xpr\x18\x01 \x01(\x0b\x32\x19.spark.connect.Expression\x12\'\n\x04type\x18\x02 \x01(\x0b\x32\x17.spark.connect.DataTypeH\x00\x12\x12\n\x08type_str\x18\x03 \x01(\tH\x00\x42\x0e\n\x0c\x63\x61st_to_type\x1a\xd9\t\n\x07Literal\x12\'\n\x04null\x18\x01 \x01(\x0b\x32\x17.spark.connect.DataTypeH\x00\x12\x10\n\x06\x62inary\x18\x02 \x01(\x0cH\x00\x12\x11\n\x07\x62oolean\x18\x03 \x01(\x08H\x00\x12\x0e\n\x04\x62yte\x18\x04 \x01(\x05H\x00\x12\x0f\n\x05short\x18\x05 \x01(\x05H\x00\x12\x11\n\x07integer\x18\x06 \x01(\x05H\x00\x12\x0e\n\x04long\x18\x07 \x01(\x03H\x00\x12\x0f\n\x05\x66loat\x18\n \x01(\x02H\x00\x12\x10\n\x06\x64ouble\x18\x0b \x01(\x01H\x00\x12<\n\x07\x64\x65\x63imal\x18\x0c \x01(\x0b\x32).spark.connect.Expression.Literal.DecimalH\x00\x12\x10\n\x06string\x18\r \x01(\tH\x00\x12\x0e\n\x04\x64\x61te\x18\x10 \x01(\x05H\x00\x12\x13\n\ttimestamp\x18\x11 \x01(\x03H\x00\x12\x17\n\rtimestamp_ntz\x18\x12 \x01(\x03H\x00\x12O\n\x11\x63\x61lendar_interval\x18\x13 \x01(\x0b\x32\x32.spark.connect.Expression.Literal.CalendarIntervalH\x00\x12\x1d\n\x13year_month_interval\x18\x14 \x01(\x05H\x00\x12\x1b\n\x11\x64\x61y_time_interval\x18\x15 \x01(\x03H\x00\x12\x38\n\x05\x61rray\x18\x16 \x01(\x0b\x32\'.spark.connect.Expression.Literal.ArrayH\x00\x12\x34\n\x03map\x18\x17 \x01(\x0b\x32%.spark.connect.Expression.Literal.MapH\x00\x12:\n\x06struct\x18\x18 \x01(\x0b\x32(.spark.connect.Expression.Literal.StructH\x00\x1a\\\n\x07\x44\x65\x63imal\x12\r\n\x05value\x18\x01 \x01(\t\x12\x16\n\tprecision\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05scale\x18\x03 \x01(\x05H\x01\x88\x01\x01\x42\x0c\n\n_precisionB\x08\n\x06_scale\x1a\x46\n\x10\x43\x61lendarInterval\x12\x0e\n\x06months\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ys\x18\x02 \x01(\x05\x12\x14\n\x0cmicroseconds\x18\x03 \x01(\x03\x1ak\n\x05\x41rray\x12-\n\x0c\x65lement_type\x18\x01 \x01(\x0b\x32\x17.spark.connect.DataType\x12\x33\n\x08\x65lements\x18\x02 \x03(\x0b\x32!.spark.connect.Expression.Literal\x1a\xc1\x01\n\x03Map\x12)\n\x08key_type\x18\x01 \x01(\x0b\x32\x17.spark.connect.DataType\x12+\n\nvalue_type\x18\x02 \x01(\x0b\x32\x17.spark.connect.DataType\x12/\n\x04keys\x18\x03 \x03(\x0b\x32!.spark.connect.Expression.Literal\x12\x31\n\x06values\x18\x04 \x03(\x0b\x32!.spark.connect.Expression.Literal\x1ak\n\x06Struct\x12,\n\x0bstruct_type\x18\x01 \x01(\x0b\x32\x17.spark.connect.DataType\x12\x33\n\x08\x65lements\x18\x02 \x03(\x0b\x32!.spark.connect.Expression.LiteralB\x0e\n\x0cliteral_type\x1aT\n\x13UnresolvedAttribute\x12\x1b\n\x13unparsed_identifier\x18\x01 \x01(\t\x12\x14\n\x07plan_id\x18\x02 \x01(\x03H\x00\x88\x01\x01\x42\n\n\x08_plan_id\x1a\x90\x01\n\x12UnresolvedFunction\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12,\n\targuments\x18\x02 \x03(\x0b\x32\x19.spark.connect.Expression\x12\x13\n\x0bis_distinct\x18\x03 \x01(\x08\x12 \n\x18is_user_defined_function\x18\x04 \x01(\x08\x1a&\n\x10\x45xpressionString\x12\x12\n\nexpression\x18\x01 \x01(\t\x1a\x42\n\x0eUnresolvedStar\x12\x1c\n\x0funparsed_target\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x12\n\x10_unparsed_target\x1a\x45\n\x0fUnresolvedRegex\x12\x10\n\x08\x63ol_name\x18\x01 \x01(\t\x12\x14\n\x07plan_id\x18\x02 \x01(\x03H\x00\x88\x01\x01\x42\n\n\x08_plan_id\x1aq\n\x16UnresolvedExtractValue\x12(\n\x05\x63hild\x18\x01 \x01(\x0b\x32\x19.spark.connect.Expression\x12-\n\nextraction\x18\x02 \x01(\x0b\x32\x19.spark.connect.Expression\x1a\x8d\x01\n\x0cUpdateFields\x12\x34\n\x11struct_expression\x18\x01 \x01(\x0b\x32\x19.spark.connect.Expression\x12\x12\n\nfield_name\x18\x02 \x01(\t\x12\x33\n\x10value_expression\x18\x03 \x01(\x0b\x32\x19.spark.connect.Expression\x1a\x62\n\x05\x41lias\x12\'\n\x04\x65xpr\x18\x01 \x01(\x0b\x32\x19.spark.connect.Expression\x12\x0c\n\x04name\x18\x02 \x03(\t\x12\x15\n\x08metadata\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_metadata\x1a\x89\x01\n\x0eLambdaFunction\x12+\n\x08\x66unction\x18\x01 \x01(\x0b\x32\x19.spark.connect.Expression\x12J\n\targuments\x18\x02 \x03(\x0b\x32\x37.spark.connect.Expression.UnresolvedNamedLambdaVariable\x1a\x33\n\x1dUnresolvedNamedLambdaVariable\x12\x12\n\nname_parts\x18\x01 \x03(\tB\x0b\n\texpr_type\"\xa0\x02\n\x1f\x43ommonInlineUserDefinedFunction\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x15\n\rdeterministic\x18\x02 \x01(\x08\x12,\n\targuments\x18\x03 \x03(\x0b\x32\x19.spark.connect.Expression\x12.\n\npython_udf\x18\x04 \x01(\x0b\x32\x18.spark.connect.PythonUDFH\x00\x12\x39\n\x10scalar_scala_udf\x18\x05 \x01(\x0b\x32\x1d.spark.connect.ScalarScalaUDFH\x00\x12*\n\x08java_udf\x18\x06 \x01(\x0b\x32\x16.spark.connect.JavaUDFH\x00\x42\n\n\x08\x66unction\"q\n\tPythonUDF\x12,\n\x0boutput_type\x18\x01 \x01(\x0b\x32\x17.spark.connect.DataType\x12\x11\n\teval_type\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ommand\x18\x03 \x01(\x0c\x12\x12\n\npython_ver\x18\x04 \x01(\t\"\x8d\x01\n\x0eScalarScalaUDF\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12+\n\ninputTypes\x18\x02 \x03(\x0b\x32\x17.spark.connect.DataType\x12+\n\noutputType\x18\x03 \x01(\x0b\x32\x17.spark.connect.DataType\x12\x10\n\x08nullable\x18\x04 \x01(\x08\"s\n\x07JavaUDF\x12\x12\n\nclass_name\x18\x01 \x01(\t\x12\x31\n\x0boutput_type\x18\x02 \x01(\x0b\x32\x17.spark.connect.DataTypeH\x00\x88\x01\x01\x12\x11\n\taggregate\x18\x03 \x01(\x08\x42\x0e\n\x0c_output_type\"S\n\x0c\x43\x61llFunction\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12,\n\targuments\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionB6\n\x1eorg.apache.spark.connect.protoP\x01Z\x12internal/generatedb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spark.connect.expressions_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036org.apache.spark.connect.protoP\001Z\022internal/generated'
  _globals['_EXPRESSION']._serialized_start=105
  _globals['_EXPRESSION']._serialized_end=4683
  _globals['_EXPRESSION_WINDOW']._serialized_start=1266
  _globals['_EXPRESSION_WINDOW']._serialized_end=1940
  _globals['_EXPRESSION_WINDOW_WINDOWFRAME']._serialized_start=1503
  _globals['_EXPRESSION_WINDOW_WINDOWFRAME']._serialized_end=1940
  _globals['_EXPRESSION_WINDOW_WINDOWFRAME_FRAMEBOUNDARY']._serialized_start=1744
  _globals['_EXPRESSION_WINDOW_WINDOWFRAME_FRAMEBOUNDARY']._serialized_end=1859
  _globals['_EXPRESSION_WINDOW_WINDOWFRAME_FRAMETYPE']._serialized_start=1861
  _globals['_EXPRESSION_WINDOW_WINDOWFRAME_FRAMETYPE']._serialized_end=1940
  _globals['_EXPRESSION_SORTORDER']._serialized_start=1943
  _globals['_EXPRESSION_SORTORDER']._serialized_end=2336
  _globals['_EXPRESSION_SORTORDER_SORTDIRECTION']._serialized_start=2141
  _globals['_EXPRESSION_SORTORDER_SORTDIRECTION']._serialized_end=2249
  _globals['_EXPRESSION_SORTORDER_NULLORDERING']._serialized_start=2251
  _globals['_EXPRESSION_SORTORDER_NULLORDERING']._serialized_end=2336
  _globals['_EXPRESSION_CAST']._serialized_start=2338
  _globals['_EXPRESSION_CAST']._serialized_end=2462
  _globals['_EXPRESSION_LITERAL']._serialized_start=2465
  _globals['_EXPRESSION_LITERAL']._serialized_end=3706
  _globals['_EXPRESSION_LITERAL_DECIMAL']._serialized_start=3112
  _globals['_EXPRESSION_LITERAL_DECIMAL']._serialized_end=3204
  _globals['_EXPRESSION_LITERAL_CALENDARINTERVAL']._serialized_start=3206
  _globals['_EXPRESSION_LITERAL_CALENDARINTERVAL']._serialized_end=3276
  _globals['_EXPRESSION_LITERAL_ARRAY']._serialized_start=3278
  _globals['_EXPRESSION_LITERAL_ARRAY']._serialized_end=3385
  _globals['_EXPRESSION_LITERAL_MAP']._serialized_start=3388
  _globals['_EXPRESSION_LITERAL_MAP']._serialized_end=3581
  _globals['_EXPRESSION_LITERAL_STRUCT']._serialized_start=3583
  _globals['_EXPRESSION_LITERAL_STRUCT']._serialized_end=3690
  _globals['_EXPRESSION_UNRESOLVEDATTRIBUTE']._serialized_start=3708
  _globals['_EXPRESSION_UNRESOLVEDATTRIBUTE']._serialized_end=3792
  _globals['_EXPRESSION_UNRESOLVEDFUNCTION']._serialized_start=3795
  _globals['_EXPRESSION_UNRESOLVEDFUNCTION']._serialized_end=3939
  _globals['_EXPRESSION_EXPRESSIONSTRING']._serialized_start=3941
  _globals['_EXPRESSION_EXPRESSIONSTRING']._serialized_end=3979
  _globals['_EXPRESSION_UNRESOLVEDSTAR']._serialized_start=3981
  _globals['_EXPRESSION_UNRESOLVEDSTAR']._serialized_end=4047
  _globals['_EXPRESSION_UNRESOLVEDREGEX']._serialized_start=4049
  _globals['_EXPRESSION_UNRESOLVEDREGEX']._serialized_end=4118
  _globals['_EXPRESSION_UNRESOLVEDEXTRACTVALUE']._serialized_start=4120
  _globals['_EXPRESSION_UNRESOLVEDEXTRACTVALUE']._serialized_end=4233
  _globals['_EXPRESSION_UPDATEFIELDS']._serialized_start=4236
  _globals['_EXPRESSION_UPDATEFIELDS']._serialized_end=4377
  _globals['_EXPRESSION_ALIAS']._serialized_start=4379
  _globals['_EXPRESSION_ALIAS']._serialized_end=4477
  _globals['_EXPRESSION_LAMBDAFUNCTION']._serialized_start=4480
  _globals['_EXPRESSION_LAMBDAFUNCTION']._serialized_end=4617
  _globals['_EXPRESSION_UNRESOLVEDNAMEDLAMBDAVARIABLE']._serialized_start=4619
  _globals['_EXPRESSION_UNRESOLVEDNAMEDLAMBDAVARIABLE']._serialized_end=4670
  _globals['_COMMONINLINEUSERDEFINEDFUNCTION']._serialized_start=4686
  _globals['_COMMONINLINEUSERDEFINEDFUNCTION']._serialized_end=4974
  _globals['_PYTHONUDF']._serialized_start=4976
  _globals['_PYTHONUDF']._serialized_end=5089
  _globals['_SCALARSCALAUDF']._serialized_start=5092
  _globals['_SCALARSCALAUDF']._serialized_end=5233
  _globals['_JAVAUDF']._serialized_start=5235
  _globals['_JAVAUDF']._serialized_end=5350
  _globals['_CALLFUNCTION']._serialized_start=5352
  _globals['_CALLFUNCTION']._serialized_end=5435
# @@protoc_insertion_point(module_scope)
