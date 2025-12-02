# Play: Papa - setup

- hosts: db
  become: false
  vars:
    app_name: "papa_app"
    retry_count: 5

  tasks:
    - name: Ensure hazel-task-1 is present
      ansible.builtin.file:
        path: /opt/papa/hazel-task-1
        state: directory

    - name: Template hazel-task-1 config
      ansible.builtin.template:
        src: templates/hazel-task-1.j2
        dest: /etc/papa/hazel-task-1.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure hazel-task-2 is present
      ansible.builtin.file:
        path: /opt/papa/hazel-task-2
        state: directory

    - name: Template hazel-task-2 config
      ansible.builtin.template:
        src: templates/hazel-task-2.j2
        dest: /etc/papa/hazel-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart papa service
      ansible.builtin.service:
        name: papa
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:43Z
