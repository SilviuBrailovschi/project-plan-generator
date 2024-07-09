from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("OpenLLM-Ro/RoGemma-7b-Instruct")
model = AutoModelForCausalLM.from_pretrained("OpenLLM-Ro/RoGemma-7b-Instruct",
                                             config={"hidden_activation": "gelu_pytorch_tanh"})

instruction = "Ce jocuri de societate pot juca cu prietenii mei?"
chat = [
    {"role": "user", "content": instruction},
]
prompt = tokenizer.apply_chat_template(chat, tokenize=False, system_message="")

inputs = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
outputs = model.generate(input_ids=inputs, max_new_tokens=128)
print("raspuns:", tokenizer.decode(outputs[0]))
