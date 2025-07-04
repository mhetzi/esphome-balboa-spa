import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

DEPENDENCIES = ['uart']

CONF_SPA_ID = "balboa_spa_id"

balboa_spa_ns = cg.esphome_ns.namespace('balboa_spa')
BalboaSpa = balboa_spa_ns.class_('BalboaSpa', cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(BalboaSpa)
}).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)
