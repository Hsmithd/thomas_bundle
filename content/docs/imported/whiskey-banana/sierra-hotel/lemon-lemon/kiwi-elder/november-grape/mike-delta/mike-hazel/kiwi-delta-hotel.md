# Play: Kiwi - setup

- hosts: db
  become: false
  vars:
    app_name: "kiwi_app"
    retry_count: 2

  tasks:
    - name: Ensure banana-task-1 is present
      ansible.builtin.file:
        path: /opt/kiwi/banana-task-1
        state: directory

    - name: Template banana-task-1 config
      ansible.builtin.template:
        src: templates/banana-task-1.j2
        dest: /etc/kiwi/banana-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure victor-task-2 is present
      ansible.builtin.file:
        path: /opt/kiwi/victor-task-2
        state: directory

    - name: Template victor-task-2 config
      ansible.builtin.template:
        src: templates/victor-task-2.j2
        dest: /etc/kiwi/victor-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart kiwi service
      ansible.builtin.service:
        name: kiwi
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:44Z
