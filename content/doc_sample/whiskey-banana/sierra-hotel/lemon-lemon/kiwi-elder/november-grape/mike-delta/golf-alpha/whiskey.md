# Play: Whiskey - setup

- hosts: all
  become: true
  vars:
    app_name: "whiskey_app"
    retry_count: 5

  tasks:
    - name: Ensure papa-task-1 is present
      ansible.builtin.file:
        path: /opt/whiskey/papa-task-1
        state: directory

    - name: Template papa-task-1 config
      ansible.builtin.template:
        src: templates/papa-task-1.j2
        dest: /etc/whiskey/papa-task-1.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure jasmine-task-2 is present
      ansible.builtin.file:
        path: /opt/whiskey/jasmine-task-2
        state: directory

    - name: Template jasmine-task-2 config
      ansible.builtin.template:
        src: templates/jasmine-task-2.j2
        dest: /etc/whiskey/jasmine-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart whiskey service
      ansible.builtin.service:
        name: whiskey
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
